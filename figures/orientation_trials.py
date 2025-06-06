import os
import sys
sys.path.insert(0, "../codes/")
import random
import numpy as np
import unit_sphere
import rotation
import matplotlib.pyplot as plt
from matplotlib import rc
rc("font",**{"family":"sans-serif","sans-serif":["OpenSans"]})
rc("text", usetex=True)
basename = os.path.basename(__file__)[:-3]
random.seed(43279857)
num_sims = 20
num_trials = int(5e5)
num_bins = int(3e2)
#num_bins = int(num_trials/1e3)
def atan2(xs): return np.atan2(xs[:, 1], xs[:, 0])
def acos(xs): return np.acos(xs[:, 2])
def azimuth(an): return 0*an + 0.5/np.pi
def polar(an): return 0.5*np.sin(an)
angs = {"azimuth1": {"min":-np.pi, "fn":atan2, "dist":azimuth, "color":"blue", "i":0},
        "azimuth2": {"min":-np.pi, "fn":atan2, "dist":azimuth, "color":"green", "i":1},
        "polar1": {"min":0, "fn":acos, "dist":polar, "color":"red", "i":0},
        "polar2": {"min":0, "fn":acos, "dist":polar, "color":"orange", "i":1}}
hist = np.zeros(shape=(num_sims, len(angs), 2, num_bins))
for sim in range(num_sims):
    x = [[1, 0, 0], [0, 1, 0]]
    xyz = np.zeros(shape=(num_trials, 2, 3))
    dt_max = np.pi
    for ixyz,_ in enumerate(xyz):
        angle = dt_max*random.uniform(-0.5, 0.5)
        dt_max = np.pi/10
        axis = unit_sphere.uniform_surface()
        for ix,_ in enumerate(x):
            x[ix] = np.matmul(rotation.axis_angle(axis, angle), x[ix])
            xyz[ixyz][ix] = x[ix]
    #for ix in [0]:
    #for ix,_ in enumerate(x):
    for ia,a in enumerate(angs):
        cn, bn = np.histogram(angs[a]["fn"](xyz[:, angs[a]["i"]]), bins=num_bins, density=True, range=[angs[a]["min"],np.pi])
        hist[sim][ia][0] = bn[1:] - 0.5*(bn[1] - bn[0])
        hist[sim][ia][1] = cn
for ia,a in enumerate(angs):
    mean = np.zeros(num_bins)
    std = np.zeros(num_bins)
    inside = 0
    bins = hist[0, ia, 0, :]
    for bn in range(num_bins):
        mean[bn] = np.mean(hist[:, ia, 1, bn])
        std[bn] = np.std(hist[:, ia, 1, bn])/np.sqrt(num_sims)
        inside += np.abs(mean[bn] - angs[a]["dist"](bins[bn])) < std[bn]
    print("Percent", a, "within a stdev:", inside/num_bins)
    plt.errorbar(bins, mean, std, fmt=".", color=angs[a]["color"], zorder=0)
    plt.plot(bins, angs[a]["dist"](bins), color="black", zorder=1)
#plt.show()
plt.xlabel("Angle", fontsize=16)
plt.ylabel("Probability Density", fontsize=16)
plt.annotate("Polar Angles", xy=[1, 0.45], xytext=[-1.1, 0.5], arrowprops=dict(arrowstyle="->", lw=1), fontsize=16)
plt.annotate("Azimuthal Angles", xy=[-1.5, 0.2], xytext=[-2.5, 0.3], arrowprops=dict(arrowstyle="->", lw=1), fontsize=16)
plt.savefig(basename+".pdf", transparent=True, dpi=300)
