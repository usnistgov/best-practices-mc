import numpy as np
import matplotlib.pyplot as plt
import quaternion
import rotation_matrix
import unit_sphere
ax = plt.figure().add_subplot(projection='3d')
unit_sphere.plot(ax)
x = np.empty(shape=(int(1e3), 3))
for i, _ in enumerate(x):
    q = [0, 0, 0, 1] + 0.3*quaternion.rand()
    q /= np.linalg.norm(q)
    z = [0, 0, 1]
    x[i] = np.matmul(rotation_matrix.R_from_quat(q), z)
ax.scatter(x[:, 0], x[:, 1], x[:, 2], color='orange')
plt.show()
