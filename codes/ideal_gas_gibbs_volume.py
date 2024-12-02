import random
import numpy as np
from statistics import block
random.seed(43279857)
N1 = random.randint(2, 3)
N2 = random.randint(4, 5)
V_total = float(N1 + N2)
V1 = float(N1)
def V2(): return V_total - V1
V1s = np.zeros(int(1e7))
dVmax = 0.1*V1
for trial_num, _ in enumerate(V1s):
    dV = random.uniform(0, dVmax)
    if random.choice([1, 2]) == 1:
        chi = ((V1-dV)/V1)**N1*((V2()+dV)/V2())**N2
        if V1 > dV and random.random() < chi:
            V1 -= dV
    else:
        chi = ((V2()-dV)/V2())**N2*((V1+dV)/V1)**N1
        if V2() > dV and random.random() < chi:
            V1 += dV
    V1s[trial_num] = V1
print("Density 1:", block(N1/V1s))
print("Density 2:", block(N2/(V_total-V1s)))
