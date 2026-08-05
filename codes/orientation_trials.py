import random
import numpy as np
import orientation
from nvt_harmonic import mc_accept, block_avg


def init_particles():
    return np.array([[0.0, 0.0, 0.0],
                     [1.0, 0.0, 0.0],
                     [0.0, 1.0, 0.0]])

def bonds(particles):
    bond_1 = particles[1] - particles[0]
    bond_2 = particles[2] - particles[0]
    return np.array([bond_1, bond_2])

def dipole(particles):
    bond_1, bond_2 = bonds(particles)
    return (bond_1 + bond_2) / np.sqrt(2.0)

def dipole_energy(particles, beta, field):
    return -field * dipole(particles)[2] / beta

def rotate(coordinates, direction, angle):
    cos, sin = np.cos(angle), np.sin(angle)
    i, j = (direction + 1) % 3, (direction + 2) % 3
    rotated = coordinates.copy()
    rotated[:, i] = cos * coordinates[:, i] - sin * coordinates[:, j]
    rotated[:, j] = sin * coordinates[:, i] + cos * coordinates[:, j]
    return rotated

def mc_attempt_rot(old_coordinates, max_rot):
    direction = random.choice([0, 1, 2])
    angle = max_rot * random.uniform(-0.5, 0.5)
    return rotate(old_coordinates, direction, angle)

def mc_run(beta, field, n_steps, max_rot=np.pi / 2):
    particles = init_particles()
    energy = dipole_energy(particles, beta, field)

    orientations = np.zeros((n_steps, 2, 3))
    cosines = np.zeros(n_steps)
    energies = np.zeros(n_steps)

    for step in range(n_steps):
        new_particles = mc_attempt_rot(particles, max_rot)
        new_energy = dipole_energy(new_particles, beta, field)
        if mc_accept(energy, new_energy, beta):
            particles, energy = new_particles, new_energy
        orientations[step] = bonds(particles)
        cosines[step] = dipole(particles)[2]
        energies[step] = energy

    return orientations, cosines, energies

def run_sims(beta, num_sims, n_steps, num_bins=300, equil=5000):
    mids = {}
    counts = {name: np.zeros((num_sims, num_bins))
              for name in orientation.ANGLES}
    for sim in range(num_sims):
        orientations, _, _ = mc_run(beta, 0, n_steps)
        for name in orientation.ANGLES:
            mids[name], counts[name][sim] = orientation.histogram(
                orientations[equil:], name, num_bins)
    return mids, counts

def langevin(field): return 1 / np.tanh(field) - 1 / field

if __name__ == "__main__":
    random.seed(43279857)
    beta = random.uniform(1, 2)
    field = random.uniform(1, 2)

    _, cosines, energies = mc_run(beta, field, n_steps=int(1e6))
    print("Expected cos:", langevin(field))
    print("cos:", *block_avg(cosines))
    print("Expected energy:", -field * langevin(field) / beta)
    print("Energy:", *block_avg(energies))

    mids, counts = run_sims(beta, num_sims=20, n_steps=int(5e5))
    for name, (_, dist, _) in orientation.ANGLES.items():
        inside = orientation.percent_within_stdev(
            mids[name], counts[name], dist)
        print("Percent", name, "within a stdev:", inside)