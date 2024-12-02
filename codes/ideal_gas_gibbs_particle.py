import numpy as np
import random
from statistics import block
random.seed(43279857)
V1 = random.uniform(4, 6)
V2 = random.uniform(2, 3)
N_total = int(V1 + V2)
N1 = int(V1)
def N2(): return N_total - N1
N1s = np.zeros(int(1e7))
for trial_num, _ in enumerate(N1s):
    if random.choice([1, 2]) == 1:
        if N1 > 0 and random.random() < V2*N1/(N2()+1)/V1:
            N1 -= 1
    else:
        if N2() > 0 and random.random() <V1*N2()/(N1+1)/V2:
            N1 += 1
    N1s[trial_num] = N1
print("Density 1:", block(N1s/V1))
print("Density 2:", block((N_total-N1s)/V2))
