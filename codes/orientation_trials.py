import random
import numpy as np
from rotation import axis_angle
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

def mc_attempt_rot(old_coordinates, max_rot):
    axis = np.identity(3)[random.choice([0, 1, 2])]
    angle = max_rot * random.uniform(-0.5, 0.5)
    return np.matmul(old_coordinates, axis_angle(axis, angle).T)

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