def affinetrans(P, width, height):
    plist = []
    for p in P:
        x, y = p[0], p[1]
        p1, p2 = [x - 2 / 3 * width, y], [x + 2 / 3 * width, y]
        p3, p4 = [x, y - 2 / 3 * height], [x, y + 2 / 3 * height]
        plist1 = [p, p1, p2, p3, p4]
        plist.extend(plist1)
    width *= 1 / 3
    height *= 1 / 3
    return plist, width, height
def fractal(p_init, width, height):
    pf = [p_init]
    t = 0
    while t < 2:
        plist1, w1, h1 = affinetrans(pf, width, height)
        pf = plist1
        width = w1
        height = h1
        t += 1
    return pf, width, height
def DrawQuad(Plist, w, h, f):
    for pt in Plist:
        x, y = pt[0], pt[1]
        p1, p2, p3, p4 = [x - w, y], [x + w, y], [x, y - h], [x, y + h]
        f.writelines(['\n    <polygon fill="none" stroke="purple" stroke-width="1" points="', str(p1[0]), ',',
                      str(p1[1]), ' ', str(p3[0]), ',', str(p3[1]), ' ', str(p2[0]), ',', str(p2[1]), ' ', str(p4[0]),
                      ',', str(p4[1]), '"/>'])
