import os
import sys
sys.path.insert(0, "../codes/")
import random
import numpy as np
import unit_sphere
import rotation_matrix
import matplotlib.pyplot as plt
from matplotlib import rc
rc("font",**{"family":"sans-serif","sans-serif":["OpenSans"]})
rc("text", usetex=True)
basename = os.path.basename(__file__)[:-3]
random.seed(43279857)
num_sims = 10
num_bins = 100
hist = np.zeros(shape=(num_sims, 2, 2, num_bins))
def atan2(xs): return np.atan2(xs[:, 1], xs[:, 0])
def acos(xs): return np.acos(xs[:, 2])
def theta_dist(an): return 0*an + 0.5/np.pi
def phi_dist(an): return 0.5*np.sin(an)
angs = {"theta": {"min":-np.pi, "fn":atan2, "dist":theta_dist, "color":"blue"},
        "phi": {"min":0, "fn":acos, "dist":phi_dist, "color":"red"}}
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
    av = np.zeros(num_bins)
    std = np.zeros(num_bins)
    inside = 0
    bins = hist[0, ia, 0, :]
    for bn in range(num_bins):
        av[bn] = np.mean(hist[:, ia, 1, bn])
        std[bn] = np.std(hist[:, ia, 1, bn])/np.sqrt(num_sims)
        inside += np.abs(av[bn] - angs[a]["dist"](bins[bn])) < std[bn]
    print("Percent", a, "within a stdev:", inside/num_bins)
    plt.errorbar(bins, av, std, fmt=".", color=angs[a]["color"])
    plt.plot(bins, angs[a]["dist"](bins), color="black")
#plt.show()
plt.xlabel("Angle", fontsize=16)
plt.ylabel("Probability Density", fontsize=16)
plt.annotate("Polar Angle", xy=[1, 0.45], xytext=[-1.1, 0.5], arrowprops=dict(arrowstyle="->", lw=1), fontsize=16)
plt.annotate("Azimuthal Angle", xy=[-1.5, 0.2], xytext=[-2.5, 0.3], arrowprops=dict(arrowstyle="->", lw=1), fontsize=16)
plt.savefig(basename+".pdf", transparent=True, dpi=300)
