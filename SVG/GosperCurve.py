import numpy as np
import math
def rot(alpha, veci):
    c, s = np.cos(alpha), np.sin(alpha)
    mat = np.array([[c, s], [-s, c]])
    vec = np.dot(veci, mat)
    return vec
def basicFrac(llist):
    plist = []
    ki = [0,0,1,1,0,1,1, 1,0,0,1, 0,0,1,0,0,0,1,1]*100
    llist1 = []
    for i in range(len(llist)):
        if ki[i] == 0:
            sp, ep = [llist[i][0], llist[i][1]], [llist[i][2], llist[i][3]]
        else:
            sp, ep = [llist[i][2], llist[i][3]], [llist[i][0], llist[i][1]]
        theta = [0, 60, 0, 60, 60, 0, 120, 60, 240, -60, -60, 0, -60, -60, 0, 0, -60,0]
        theta = [np.radians(x) for x in theta]
        alpha = -math.atan2(np.sqrt(3), 4)
        sp, ep = np.array(sp), np.array(ep)
        vec = ep - sp
        v1 = rot(alpha, vec)/np.sqrt(19)
        l1p = v1+sp
        llist1.append([sp[0], sp[1], l1p[0], l1p[1]])
        for j in theta:
            v1 = rot(j, v1)
            llist1.append([l1p[0],l1p[1], l1p[0]+v1[0], l1p[1]+v1[1]])
            l1p += v1
    return llist1
#while loop
def frac(llist):
    t = 0
    while t<2:
        llist = basicFrac(llist)
        t += 1
    return llist
