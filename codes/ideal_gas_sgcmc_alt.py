import random
import numpy as np
from statistics import block
random.seed(43279857)
vz1 = random.uniform(10, 20)
vz2 = random.uniform(10, 20)
N1 = int(vz1)
N = N1 + int(vz2)
def N2(): return N - N1
print("Analytical fraction:", vz1/(vz1+vz2))
N1s = np.zeros(int(1e6))
for trial, _ in enumerate(N1s):
    if random.choice(["1to2", "2to1"]) == "1to2":
        if N1 > 0 and random.random() < N1/(N2() + 1)*vz2/vz1:
            N1 -= 1
    else:
        if N2() > 0 and random.random() < N2()/(N1 + 1)*vz1/vz2:
            N1 += 1
    N1s[trial] = N1
print("Numerical fraction:", block(N1s/N))
