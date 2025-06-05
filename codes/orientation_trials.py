import random
import numpy as np
import unit_sphere
import rotation_matrix
random.seed(43279857)
num_sims = 10
num_bins = 100
hist = np.zeros(shape=(num_sims, 2, 2, num_bins))
def atan2(xs): return np.atan2(xs[:, 1], xs[:, 0])
def acos(xs): return np.acos(xs[:, 2])
def theta_dist(an): return 0*an + 0.5/np.pi
def phi_dist(an): return 0.5*np.sin(an)
angs = {"theta": {"min":-np.pi, "fn":atan2, "dist":theta_dist},
        "phi": {"min":0, "fn":acos, "dist":phi_dist}}
for sim in range(num_sims):
    x = [0, 0, 1]
    xyz = np.zeros(shape=(int(1e6), 3))
    for ix,_ in enumerate(xyz):
        angle = random.uniform(0, np.pi/10)
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
        av = np.mean(hist[:, ia, 1, ib])
        std = np.std(hist[:, ia, 1, ib])/np.sqrt(num_sims)
        inside += np.abs(av - angs[a]["dist"](b)) < std
    print("Percent", a, "within a stdev:", inside/num_bins)
