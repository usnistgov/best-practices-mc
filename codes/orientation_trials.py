import random
import numpy as np
import unit_sphere
import rotation_matrix
random.seed(43279857)
num_sims = 10
num_trials = int(1e6)
num_bins = int(3e2)
hist = np.zeros(shape=(num_sims, 2, 2, num_bins))
def atan2(xs): return np.atan2(xs[:, 1], xs[:, 0])
def acos(xs): return np.acos(xs[:, 2])
def azimuth_dist(an): return 0*an + 0.5/np.pi
def polar_dist(an): return 0.5*np.sin(an)
angs = {"azimuth": {"min":-np.pi, "fn":atan2, "dist":azimuth_dist},
        "polar": {"min":0, "fn":acos, "dist":polar_dist}}
for sim in range(num_sims):
    x = unit_sphere.uniform_surface()
    xyz = np.zeros(shape=(num_trials, 3))
    for ix,_ in enumerate(xyz):
        angle = np.pi/10*random.uniform(-0.5, 0.5)
        axis = unit_sphere.uniform_surface()
        x = np.matmul(rotation_matrix.axis_angle(axis, angle), x)
        xyz[ix] = x
    for ia,a in enumerate(angs):
        counts, bins = np.histogram(angs[a]["fn"](xyz), bins=num_bins, density=True, range=[angs[a]["min"],np.pi])
        hist[sim][ia][0] = bins[1:] - 0.5*(bins[1] - bins[0])
        hist[sim][ia][1] = counts
for ia,a in enumerate(angs):
    inside = 0
    for ib,b in enumerate(hist[0, ia, 0, :]):
        mean = np.mean(hist[:, ia, 1, ib])
        std = np.std(hist[:, ia, 1, ib])/np.sqrt(num_sims)
        inside += np.abs(mean - angs[a]["dist"](b)) < std
    print("Percent", a, "within a stdev:", inside/num_bins)
