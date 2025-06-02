import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)
basename = os.path.basename(__file__)[:-3]

shift=6
xyzs=[
[-0.01, 1.75],
[-1.6, 1.5],
[-1.4, 0.4],
[-1.2, -0.6],
[-1.7, -1.45],
[-0.4, -1.3],
[0.8, -1.45],
[1, 0.6],
[1.3, 1.6],
[1.2, -0.5],
]
pbcs=[
[-1.7+4, -1.45],
[1.3, 1.6-4],
[-1.6+4, 1.5],
[-1.4+4, 0.4],
[-1.7+4, -1.45],
[-0.01, 1.75-4],
]

# excluded volume
for xyz in xyzs:
    plt.gca().add_patch(plt.Circle((xyz[0]+shift, xyz[1]), 1, fc='grey'))
for pbc in pbcs:
    plt.gca().add_patch(plt.Circle((pbc[0]+shift, pbc[1]), 1, fc='grey'))

# box
plt.gca().add_patch(plt.Rectangle(xy=(-2+shift, -2), width=4, height=4, fc='none', ec='black', lw=2))

# particles
for xyz in xyzs:
    plt.gca().add_patch(plt.Circle((xyz[0]+shift, xyz[1]),0.5, fc='black'))
for pbc in pbcs:
    plt.gca().add_patch(plt.Circle((pbc[0]+shift, pbc[1]),0.5, fc='red', edgecolor='red', fill=None, linestyle='dashed'))

# make a grid
ng=10
for ix in range(-ng, ng+1):
    x = 2*ix/ng
    for iy in range(-ng, ng+1):
        y = 2*iy/ng
        plt.gca().add_patch(plt.Circle((shift+x, y),0.05, fc='red'))

greens=[
[0, -0.2],
[0, 0],
[0, 0.2],
[0, 0.4],
[-0.2, -0.2],
[-0.2, 0],
[-0.2, 0.2],
[-0.2, 0.4],
[-0.2, 0.6],
[-0.4, 0.2],
[-0.4, 0.6],
[-0.4, 0.8],
[0.2, -0.4],
[0.2, -0.2],
]
for g in greens:
    plt.gca().add_patch(plt.Circle((g[0]+shift, g[1]),0.05, fc='blue'))
plt.axis('scaled')
plt.axis('off')
plt.savefig(basename+'.pdf', bbox_inches='tight', transparent=True)
