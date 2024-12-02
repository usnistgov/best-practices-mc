import random
import numpy as np
from statistics import block
random.seed(43279857)
Vz1 = random.uniform(10, 20)
Vz2 = random.uniform(10, 20)
N1 = int(Vz1)
N_total = N1 + int(Vz2)
def N2(): return N_total - N1
print("Analytical fraction:", Vz1/(Vz1 + Vz2))
N1s = np.zeros(int(1e6))
for trial, _ in enumerate(N1s):
    if random.random() < N1/N_total:
        if N1 > 0 and random.random() < Vz2/Vz1:
            N1 -= 1
    else:
        if N2() > 0 and random.random() < Vz1/Vz2:
            N1 += 1
    N1s[trial] = N1
print("Numerical fraction:", block(N1s/N_total))
