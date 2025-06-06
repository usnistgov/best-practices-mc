import numpy as np
def axis_angle(axis, angle):
    cos = np.cos(angle)
    sin = np.sin(angle)
    rtmx = np.empty(shape=(3,3))
    rtmx[0][0] = cos + (1-cos)*axis[0]**2
    rtmx[1][0] = (1-cos)*axis[0]*axis[1] + sin*axis[2]
    rtmx[2][0] = (1-cos)*axis[0]*axis[2] - sin*axis[1]
    rtmx[0][1] = (1-cos)*axis[0]*axis[1] - sin*axis[2]
    rtmx[1][1] = cos + (1-cos)*axis[1]**2
    rtmx[2][1] = (1-cos)*axis[1]*axis[2] + sin*axis[0]
    rtmx[0][2] = (1-cos)*axis[0]*axis[2] + sin*axis[1]
    rtmx[1][2] = (1-cos)*axis[1]*axis[2] - sin*axis[0]
    rtmx[2][2] = cos + (1-cos)*axis[2]**2
    return rtmx
