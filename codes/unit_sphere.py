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
    x = np.empty(shape=(int(1e3), 3))
    for i, _ in enumerate(x):
        x[i] = uniform_surface()
    ax.scatter(x[:, 0], x[:, 1], x[:, 2])
