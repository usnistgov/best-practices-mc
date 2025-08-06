import random
import numpy as np
import matplotlib.pyplot as plt

def uniform_surface(radius=1):
    theta = 2*np.pi*random.uniform(0, 1)
    phi = np.arccos(random.uniform(-1, 1))
    return [radius*np.sin(phi)*np.cos(theta),
            radius*np.sin(phi)*np.sin(theta),
            radius*np.cos(phi)]

def plot(ax):
    for i in range(int(1e4)):
        x = uniform_surface()
        ax.plot([0, x[0]], [0, x[1]], [0, x[2]],
                color='blue', alpha=0.025)
