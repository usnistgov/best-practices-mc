# This is copied from the codes directory, but with special font and figure graphics options
# The resulting png was also manually cropped with GIMP->zealous crop
import os
import sys
sys.path.insert(0, '../codes/')
import numpy as np
import matplotlib.pyplot as plt
import quaternion
import rotation_matrix
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
x = np.empty(shape=(int(1e3), 3))
for i, _ in enumerate(x):
    q = [0, 0, 0, 1] + 0.3*quaternion.rand()
    q /= np.linalg.norm(q)
    z = [0, 0, 1]
    x[i] = np.matmul(rotation_matrix.R_from_quat(q), z)
ax.scatter(x[:, 0], x[:, 1], x[:, 2], color='orange')
plt.axis('scaled')
plt.axis('off')
plt.savefig(basename+'.png', bbox_inches='tight', transparent=True, dpi=300)
