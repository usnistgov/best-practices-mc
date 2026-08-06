import random
import numpy as np
from nvt_harmonic import mc_attempt_trans, block_avg


def init_volume(number, beta, pressure):
    return number / (beta * pressure)

def mc_attempt_vol(old_volume, max_disp):
    return mc_attempt_trans(old_volume, max_disp)

def mc_attempt_ln_vol(old_volume, max_disp):
    return np.exp(mc_attempt_trans(np.log(old_volume), max_disp))

def mc_accept_vol(old_volume, new_volume, beta, pressure, factor):
    ln_acceptance = (-beta * pressure * (new_volume - old_volume)
                     + factor * np.log(new_volume / old_volume))
    return random.random() < np.exp(ln_acceptance)

def mc_run(beta, pressure, number, factor, n_steps, mc_attempt,
           max_disp=3):
    volume = init_volume(number, beta, pressure)
    volumes = np.zeros(n_steps)
    for step in range(n_steps):
        new_volume = mc_attempt(volume, max_disp)
        if new_volume > 0:
            if mc_accept_vol(volume, new_volume, beta, pressure,
                             factor):
                volume = new_volume
        volumes[step] = volume
    return volumes

if __name__ == "__main__":
    random.seed(43279857)
    number = random.uniform(2, 3)
    beta = random.uniform(1, 2)
    pressure = random.uniform(0.25, 0.5)
    print("Ideal gas volume:", init_volume(number, beta, pressure))
    
    for name, att, fac in [("V", mc_attempt_vol, number - 1),
                           ("lnV", mc_attempt_ln_vol, number)]:
        v = mc_run(beta, pressure, number, fac, int(1e6), att)
        print("Volume,", name, ":", *block_avg(v))