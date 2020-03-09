import svgFunc, fractal, GosperCurve
from svgFunc import polygon_, genelist, line_,rect_, text_,image_
from fractal import fractal, DrawQuad
from GosperCurve import frac
#l = int(input('Enter the length of the box:'))
#w = int(input('Enter the width of the box:'))
#h = int(input('Enter the height of the box:'))
#t = int(input('Enter the thickness of the box:'))
#l,w,h,t =160,100,80,2#(the first box)'; 200,140,95,2(2nd)
l,w,h,t = 200, 140, 95, 2

#Open file
f = open('Box.svg','w')
f.write('<?xml version="1.0" encoding="UTF-8" ?>')
f.write('\n<svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink">')

#generate layout of the box
vec = [200, 100]
pl, ll, rl = genelist(l, w, h, t)
polygon_(pl, vec, f)
line_(ll, vec, f)
rect_(rl, 21, 2, vec, f)
r1 = [[-w/2-h+10, pl[4][1]+l*5/8], [w/2+h-30, pl[4][1]+l*5/8]]
rect_(r1, 20, l/4, vec, f)

#draw fractal1
hs = 1/2*h
#hs = 1/2*h####
#vec_f = [vec[0]+w/2+h/4+10, vec[1]+pl[4][1]+l/2]
#p1, w1, h1=fractal(vec_f, 25, 50)
#DrawQuad(p1, w1, h1, f)
# fractal2
l_init = [[w/2+3, pl[4][1]+l*2/8+20, w/2+h-20, pl[4][1]+l*2/8+20]]
llist = frac(l_init)
line_(llist,vec,f)

#text
vect = [[vec[0], vec[1]+pl[14][1]-h/4],[vec[0], vec[1]+pl[14][1]-h/4+13], [vec[0], vec[1]+pl[4][1]-hs/2], \
        [vec[0]-w/2-h/8, vec[1]+pl[4][1]+l/2], [vec[0], vec[1]+pl[12][1]+h/2-10], [vec[0], vec[1]+pl[12][1]+h/2+10]]
#vect = [[vec[0], vec[1]+pl[14][1]-h/4],[vec[0], vec[1]+pl[14][1]-h/4+13], [vec[0], vec[1]+pl[4][1]-hs/2], \
#[vec[0]-w/2-h/8, vec[1]+pl[4][1]+l/2], [vec[0]+w/4, vec[1]+pl[12][1]+h/2-25], [vec[0]+w/4, vec[1]+pl[12][1]+h/2-30]\
 #       [vec[0]-w/2-h*5/16, vec[1]+pl[4][1]+l/2]]
txt=['Digital', 'Manufacturing', 'Gigi - 2', '8 - K.Bryant -24', 'L.Pan', 'L.Shen']#box1
#txt=['Digital', 'Manufacturing', "Keep moving. Dont't settle",'CARPE DIEM', '', '','']
rot = [0, 0, 0, -90, 180, 180, -90]
font = [13, 13, 11, 13, 11, 11, 13]
for i in range(len(vect)):
    text_(vect[i], txt[i], rot[i], font[i], f)

#image
image_([vec[0]-50, vec[1]+pl[14][1]-h+10], 100, 40, 0, 'https://www.nicepng.com/png/detail/141-1417263_filecolumbia-crown-simple-columbia-university-logo.png', f)
image_([vec[0]-w/2-h/2-10, vec[1]+pl[7][1]+l/4], 28, 40, 0, 'https://i.pinimg.com/236x/69/b6/49/69b64998a7c08c20b564647c23a7a3e3.jpg', f)
#image_([vec[0]-w/2-h/2-10, vec[1]+pl[7][1]+l/4], 28, 40, 0, 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSRCTLJwLm5lZqDs5LjxP25Xb3u-C41c15kOE2h1BR4HprJPfW7', f)

# close file
f.write('\n</svg>')
f.close()
