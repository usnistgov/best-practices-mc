import numpy as np
from rotation import axis_angle


def azimuth(bonds):
    return np.arctan2(bonds[:, 0, 1], bonds[:, 0, 0])

def polar(bonds):
    return np.arccos(bonds[:, 0, 2])

def psi(bonds):
    """Azimuthal angle of the second bond in the reference frame
    given by the minimal rotation of the z-axis into the first
    bond."""
    angles = np.zeros(len(bonds))
    z = np.array([0.0, 0.0, 1.0])
    for i, (bond_1, bond_2) in enumerate(bonds):
        axis = np.cross(z, bond_1)
        axis /= np.linalg.norm(axis)
        rtmx = axis_angle(axis, np.arccos(np.dot(z, bond_1)))
        angles[i] = np.arctan2(
            np.dot(bond_2, np.matmul(rtmx, [1, 0, 0])),
            np.dot(bond_2, np.matmul(rtmx, [0, 1, 0])))
    return angles


def uniform_dist(angle): return 0 * angle + 0.5 / np.pi

def sine_dist(angle): return 0.5 * np.sin(angle)

ANGLES = {"azimuth": (azimuth, uniform_dist, -np.pi),
          "polar": (polar, sine_dist, 0),
          "psi": (psi, uniform_dist, -np.pi)}

def histogram(bonds, name, num_bins):
    angle_fn, _, low = ANGLES[name]
    counts, bins = np.histogram(angle_fn(bonds), bins=num_bins,
                                density=True, range=[low, np.pi])
    return bins[1:] - 0.5 * (bins[1] - bins[0]), counts

def percent_within_stdev(mids, counts, dist):
    mean = np.average(counts, axis=0)
    stdev = np.std(counts, axis=0) / np.sqrt(len(counts))
    return np.average(np.abs(mean - dist(mids)) < stdev)