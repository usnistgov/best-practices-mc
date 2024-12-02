import numpy as np
def R_from_quat(q):
    rm = np.empty(shape=(3,3))
    rm[0][0] = q[0]*q[0] - q[1]*q[1] - q[2]*q[2] +q[3]*q[3]
    rm[1][0] = 2*(q[0]*q[1] + q[2]*q[3])
    rm[2][0] = 2*(q[2]*q[0] - q[1]*q[3])
    rm[0][1] = 2*(q[0]*q[1] - q[2]*q[3])
    rm[1][1] = q[1]*q[1] - q[2]*q[2] - q[0]*q[0] +q[3]*q[3]
    rm[2][1] = 2*(q[1]*q[2] + q[0]*q[3])
    rm[0][2] = 2*(q[2]*q[0] + q[1]*q[3])
    rm[1][2] = 2*(q[1]*q[2] - q[0]*q[3])
    rm[2][2] = q[2]*q[2] - q[0]*q[0] - q[1]*q[1] +q[3]*q[3]
    return rm