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
for sampling in ["V", "lnV"]:
    for trial_num, _ in enumerate(V1s):
        dV = dVmax*random.uniform(-1, 1)
        factor = N1
        if sampling != "V":
            dV = V1*np.exp(dV) - V1
            factor += 1
        chi = ((V1+dV)/V1)**factor*((V2()-dV)/V2())**N2
        if V1 > -dV and V2() > dV and random.random() < chi:
            V1 += dV
        V1s[trial_num] = V1
    print('Sampling:', sampling)
    print("Density 1:", block(N1/V1s))
    print("Density 2:", block(N2/(V_total-V1s)))
