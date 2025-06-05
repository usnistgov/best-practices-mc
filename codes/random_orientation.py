import numpy as np
import matplotlib.pyplot as plt
import unit_sphere
import random
import rotation_matrix
random.seed(43279857)
ax = plt.figure().add_subplot(projection='3d')
unit_sphere.plot(ax)
for i in range(int(1e4)):
    angle = random.uniform(0, np.pi/2.)
    axis = unit_sphere.uniform_surface()
    x = np.matmul(rotation_matrix.axis_angle(axis, angle), [0, 0, 1])
    ax.plot([0, x[0]], [0, x[1]], [0, x[2]],
            color='orange', alpha=0.025)
ax.plot([0,0], [0,0], [0,1], color='black')
plt.show()
