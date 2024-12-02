import random
import numpy as np
def rand():
    q = np.empty(4)
    s1 = 2
    while s1 > 1:
      q[0] = random.uniform(-1, 1)
      q[1] = random.uniform(-1, 1)
      s1 = q[0]**2 + q[1]**2
    s2 = 2
    while s2 > 1:
      q[2] = random.uniform(-1, 1)
      q[3] = random.uniform(-1, 1)
      s2 = q[2]**2 + q[3]**2
    s1 = np.sqrt((1 - s1)/s2)
    q[2] *= s1
    q[3] *= s1
    return q
