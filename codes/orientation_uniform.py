import random
import numpy as np
import orientation
from orientation_trials import mc_run


def run_sims(beta, num_sims, n_steps, num_bins=300, equil=5000):
    """Repeat the trial of Code Block 2a with no field, the ideal
    gas limit where every trial is accepted and the orientation
    is expected to be uniform. The first equil orientations of
    each simulation are discarded so that the rest are
    decorrelated from the initial one."""
    mids = {}
    counts = {name: np.zeros((num_sims, num_bins))
              for name in orientation.ANGLES}
    for sim in range(num_sims):
        orientations, _, _ = mc_run(beta, 0, n_steps)
        for name in orientation.ANGLES:
            mids[name], counts[name][sim] = orientation.histogram(
                orientations[equil:], name, num_bins)
    return mids, counts


if __name__ == "__main__":
    random.seed(43279857)
    beta = random.uniform(1, 2)
    mids, counts = run_sims(beta, num_sims=20, n_steps=int(5e5))
    for name, (_, dist, _) in orientation.ANGLES.items():
        inside = orientation.percent_within_stdev(
            mids[name], counts[name], dist)
        print("Percent", name, "within a stdev:", inside)