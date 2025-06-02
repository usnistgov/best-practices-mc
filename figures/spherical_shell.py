# This is copied from the codes directory, but with special font and figure graphics options
# The resulting png was also manually cropped with GIMP->zealous crop
import os
import sys
sys.path.insert(0, '../codes/')
import random
import numpy as np
import matplotlib.pyplot as plt
import unit_sphere
import matplotlib
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['OpenSans']})
rc('text', usetex=True)
basename = os.path.basename(__file__)[:-3]
random.seed(43279857)
r_upper = 3
r_lower = 2
x = np.empty(shape=(int(1e5), 3))
for i,_ in enumerate(x):
    radius = (random.uniform(0, 1)*(r_upper**3 - r_lower**3) + r_lower**3)**(1./3.)
    x[i] = unit_sphere.uniform_surface(radius)
ax = plt.figure().add_subplot(projection='3d')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], s=1, alpha=0.05)
plt.axis('scaled')
plt.axis('off')
plt.savefig(basename+'.png', bbox_inches='tight', transparent=True, dpi=300)
