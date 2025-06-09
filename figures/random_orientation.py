# This is copied from the codes directory, but with special font and figure graphics options
# The resulting png was also manually cropped with GIMP->zealous crop
import os
import sys
sys.path.insert(0, '../codes/')
import numpy as np
import matplotlib.pyplot as plt
import rotation
import unit_sphere
import matplotlib
import random
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)
basename = os.path.basename(__file__)[:-3]
random.seed(43279857)
ax = plt.figure().add_subplot(projection='3d')
unit_sphere.plot(ax)
for i in range(int(1e4)):
    angle = random.uniform(-np.pi/2, np.pi/2)
    axis = unit_sphere.uniform_surface()
    x = np.matmul(rotation.axis_angle(axis, angle), [0, 0, 1])
    ax.plot([0, x[0]], [0, x[1]], [0, x[2]], color='orange', alpha=0.025)
ax.plot([0,0], [0,0], [0,1], color='black')
ax.set_xlabel('x', fontsize=16)
ax.set_ylabel('y', fontsize=16)
ax.set_zlabel('z', fontsize=16)
plt.savefig(basename+'.png', transparent=True, dpi=300)
