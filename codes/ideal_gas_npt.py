import random
import numpy as np
from statistics import block
random.seed(43279857)
number = random.uniform(2, 3)
beta_pressure = random.uniform(0.25, 0.5)
print("Ideal gas volume:", number/beta_pressure)
for sampling in ["V", "lnV"]:
    vol = number/beta_pressure
    vols = np.zeros(int(1e6))
    for trial, _ in enumerate(vols):
        new_vol = vol
        if sampling == "V":
            new_vol += random.uniform(-3, 3)
            factor = number - 1
        else:
            new_vol *= np.exp(random.uniform(-3, 3))
            factor = number
        if new_vol > 0:
            bpdv = beta_pressure*(new_vol - vol)
            ln_prob = -bpdv + factor*np.log(new_vol/vol)
            if random.random() < np.exp(ln_prob):
                vol = new_vol
        vols[trial] = vol
    print("Volume:", block(vols))
