import random
import numpy as np

def init_position_harmonic(): return 0

def harmonic_energy(position, beta): return (position ** 2) / beta

def accept_prob(old_energy, new_energy, beta):
    return min(1, np.exp(-beta * (new_energy - old_energy)))

def mc_attempt_trans(old_position, max_disp):
    return old_position + random.uniform(-max_disp, max_disp)

def mc_accept(old_energy, new_energy, beta):
    acceptance = accept_prob(old_energy, new_energy, beta)
    return random.random() < acceptance

def mc_run(beta, n_steps, max_disp=0.5):
    position = init_position_harmonic()
    energy = harmonic_energy(position, beta)
    positions = np.zeros(n_steps)
    energies = np.zeros(n_steps)
    for step in range(n_steps):
        new_position = mc_attempt_trans(position, max_disp)
        new_energy = harmonic_energy(new_position, beta)
        if mc_accept(energy, new_energy, beta):
            position, energy = new_position, new_energy
        positions[step] = position
        energies[step] = energy
    return positions, energies

def block_avg(values, num_blocks=100, equil=1000):
    production = values[equil:]
    blocks = np.array_split(production, num_blocks)
    block_means = [np.average(block) for block in blocks]
    mean = np.average(production)
    standard_error = np.std(block_means) / np.sqrt(num_blocks)
    return mean, standard_error

if __name__ == "__main__":
    random.seed(43279857)
    beta = random.uniform(1, 2)
    print("Expected energy:", 0.5/beta)
    positions, energies = mc_run(beta, n_steps=int(1e6))
    mean_pos, se_pos = block_avg(positions)
    mean_en, se_en = block_avg(energies)
    print("Position:", mean_pos, "stdev", se_pos)
    print("Energy:", mean_en, "stdev", se_en)
