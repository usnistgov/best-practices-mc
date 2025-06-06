import random
import numpy as np
import unit_sphere
import rotation
random.seed(43279857)
num_sims = 20
num_trials = int(5e5)
num_bins = int(3e2)
def atan2(xs): return np.atan2(xs[:, 0, 1], xs[:, 0, 0])
def acos(xs): return np.acos(xs[:, 0, 2])
def psi(xs):
    """
    Return the azimuthal angle of second vector in a reference frame
    given by the minimal rotation of the z-axis into the first vector.
    """
    angs = np.zeros(len(xs))
    z = [0, 0, 1]
    for i,vecs in enumerate(xs):
        axis = np.cross(z, vecs[0])
        axis /= np.linalg.norm(axis)
        rtmx = rotation.axis_angle(axis, np.acos(np.dot(z, vecs[0])))
        angs[i] = np.atan2(np.dot(vecs[1], np.matmul(rtmx, [1, 0, 0])),
                           np.dot(vecs[1], np.matmul(rtmx, [0, 1, 0])))
    return angs
def azimuth(an): return 0*an + 0.5/np.pi
def polar(an): return 0.5*np.sin(an)
angs = {"azimuth": {"min":-np.pi, "fn":atan2, "dist":azimuth},
        "polar": {"min":0, "fn":acos, "dist":polar},
        "psi": {"min":-np.pi, "fn":psi, "dist":azimuth}}
hist = np.zeros(shape=(num_sims, len(angs), 2, num_bins))
for sim in range(num_sims):
    x = [[1, 0, 0], [0, 1, 0]]
    xyz = np.zeros(shape=(num_trials, 2, 3))
    dt_max = np.pi  # randomize first orientation
    for ixyz,_ in enumerate(xyz):
        angle = dt_max*random.uniform(-0.5, 0.5)
        dt_max = np.pi/10  # smaller perturbations after first
        axis = unit_sphere.uniform_surface()
        for ix,_ in enumerate(x):
            x[ix] = np.matmul(rotation.axis_angle(axis, angle), x[ix])
            xyz[ixyz][ix] = x[ix]
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
