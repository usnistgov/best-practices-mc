import random
import numpy as np
from statistics import block
random.seed(43279857)
V1 = random.uniform(20, 40)
N1 = int(V1)
V_total = V1 + random.uniform(20, 40)
def V2(): return V_total - V1
def N2(): return N_total - N1
N_total = N1 + int(V2())
N1s = np.zeros(int(1e7))
V1s = np.zeros(len(N1s))
dVmax = 0.1*V1
for trial_num, _ in enumerate(N1s):
    if random.choice(["N", "V"]) == "N":
        if random.choice([1, 2]) == 1:
            if N1 > 1:
                if random.random() < V2()*N1/(N2() + 1)/V1:
                    N1 -= 1
        else:
            if N2() > 1:
                if random.random() < V1*N2()/(N1 + 1)/V2():
                    N1 += 1
    else:
        dV = random.uniform(0, dVmax)
        if random.choice([1, 2]) == 1:
            chi = ((V1-dV)/V1)**N1* ((V2()+dV)/V2())**N2()
            if V1 > dV and random.random() < chi:
                V1 -= dV
        else:
            chi = ((V2()-dV)/V2())**N2()* ((V1+dV)/V1)**N1
            if V2() > dV and random.random() < chi:
                V1 += dV
    N1s[trial_num] = N1
    V1s[trial_num] = V1
print("N1/(N1+N2):", block(N1s/N_total))
print("V1/(V1+V2):", block(V1s/V_total))
