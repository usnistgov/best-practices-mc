import random
import numpy as np
from statistics import block
random.seed(43279857)
beta = random.uniform(1, 2)
print("Expected energy:", 0.5/beta)
positions = np.zeros(int(1e6))
energies = np.zeros(len(positions))
for trial, _ in enumerate(positions[1:]):
    delta = 0.5*random.uniform(-1., 1.)
    position_new = positions[trial-1] + delta
    energy_new = (position_new**2)/beta
    delta_energy = energy_new - energies[trial - 1]
    if random.random() < np.exp(-beta*delta_energy):
        positions[trial] = position_new
        energies[trial] = energy_new
    else:
        positions[trial] = positions[trial - 1]
        energies[trial] = energies[trial - 1]
print("Position:", block(positions))
print("Energy:", block(energies))
