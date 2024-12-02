import random
import numpy as np
import matplotlib.pyplot as plt
import unit_sphere
r_upper = 3
r_lower = 2
x = np.empty(shape=(int(1e5), 3))
for i,_ in enumerate(x):
    radius = (random.uniform(0, 1)*(r_upper**3 - r_lower**3) + r_lower**3)**(1./3.)
    x[i] = unit_sphere.uniform_surface(radius)
ax = plt.figure().add_subplot(projection='3d')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], s=1, alpha=0.05)
plt.show()
