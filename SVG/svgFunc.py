#functions for later use
def line_(llist, vec, f):
    for l in llist:
        f.writelines(['\n    <line x1="', str(l[0]+vec[0]), '" y1="', str(l[1]+vec[1]), '" x2="', str(l[2]+vec[0]),
                      '" y2="', str(l[3]+vec[1]),'" stroke="blue" stroke-width="1"/>'])

def polygon_(plist, pstart, f):
    txt = ''
    for p in plist:
        txt1 = str(p[0]+pstart[0])+','+str(p[1]+pstart[1])+' '
        txt += txt1
    f.writelines(['\n    <polygon fill="none" stroke="orange" stroke-width="1" points="', txt, '"/>'])

def rect_(startp, width, height, vec, f):
    for sp in startp:
        f.writelines(['\n    <rect x="', str(sp[0]+vec[0]),'" y="',str(sp[1]+vec[1]),'" width="',str(width),'" height="',
                      str(height), '" style="stroke-width:1;stroke:orange;fill:none"/>'])

def text_(ord, text, alpha, fontsize, f):
    f.writelines(['\n    <text x="', str(ord[0]), '" y="',str(ord[1]), '" font-size="',str(fontsize),
                  '" fill="purple" style="text-anchor: middle" transform="rotate(', str(alpha),' ',str(ord[0]),',',str(ord[1]), ')">',text, '</text>'])


def image_(coor, width, height, rot, url, f):
    f.writelines(['\n    <image x="',str(coor[0]),'" y="',str(coor[1]),'" width="',str(width),'" height="',str(height),'" transform ="rotate(',\
                 str(rot),')" xlink:href="',url,'"/>'])

def symmetry(list):
    list1 = []
    for p in list:
        p1 = [-p[0],p[1]]
        list1.append(p1)
    list1.reverse()
    list.extend(list1)
    return list

def genelist(l, w, h, t):
    hs = 1/2*h
    itv = 2*t+2#interval
    pl = 4 #plug

    #generate point list of polygon
    s1 = [10, 0]
    path = [[0, pl], [w/2-10, 0], [0, 2*hs+t+itv], [2, 0], [0, -w/2+1], [hs-2, 0], [0, w/2-1], [h-hs, l/2], [0, 1/2*l+w/2-1],\
            [-h+2, 0], [0, -w/2+1], [-2, 0], [0, 2*h+t+itv], [-w/2+10, 0], [0, pl]]
    pglist = [s1]
    for i in path:
        s1 = [s1[0]+i[0], s1[1]+i[1]]
        pglist.append(s1)
    pglist = symmetry(pglist)

    #generate list of dotline
    l1, l2, l3, l4 =[-w/2, pl+hs, w/2, pl+hs], [-w/2, pl+hs+itv, w/2, pl+hs+itv],[-w/2, pl+2*hs+itv, w/2, pl+2*hs+itv],\
                    [-w/2, pglist[12][1]+t, w/2, pglist[12][1]+t]
    l5, l6 = [-w/2, pglist[12][1]+t+h, w/2, pglist[12][1]+t+h], [-w/2, pglist[12][1]+t+h+itv, w/2, pglist[12][1]+t+h+itv]
    l7, l8 = [-w/2, pglist[4][1], -w/2, pglist[12][1]], [w/2, pglist[4][1], w/2, pglist[12][1]]
    l9, l10, l11, l12 = [-w/2-hs, pglist[4][1], -w/2-2, pglist[4][1]], [w/2+hs, pglist[4][1], w/2+2, pglist[4][1]],\
                        [-w/2-h, pglist[12][1] , -w/2-2, pglist[12][1]], [w/2+h,pglist[12][1], w/2+2, pglist[12][1]]
    llist = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    reclist = [[-10.5, 4+2*itv+2*hs], [-10.5, 5+l+2*hs]]
    return pglist, llist, reclist
