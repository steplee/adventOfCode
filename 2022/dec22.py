import sys
import numpy as np
import numpy
import re
# lines = [l.strip() for l in sys.stdin.readlines()]
lines = [l[:-1] for l in sys.stdin.readlines()]


h = len(lines)-2
w = 0
for i in range(len(lines)-1):
    line = lines[i]
    w = max(w,len(line))

a = np.zeros((h,w), dtype=int)

for i in range(len(lines)):
    line = lines[i]

    y = i
    '''
    left = -1
    end = -1
    for x in range(len(line)):
        c = line[x]
        if c == '.' or c == '#' and left == -1: left = x
    for x in range(len(line)-1,-1,-1):
        c = line[x]
        if c == '.' or c == '#' and end == -1: end = x

    for x in range(len(line)):
        p = line[x-1] if x>=1 else None
        c = line[x]
        n = line[x+1] if x<len(line)-1 else None
        if c == '.':
            d[(y,x)] = []
            # if p == ' ': d[(y,x,'l')] = 
    '''

    if i == 0:
        for x in range(len(line)):
            if line[x] == '.':
                start = (y,x)
                break

    for x in range(len(line)):
        c = line[x]
        if c == ' ': a[y,x] = 0
        if c == '.': a[y,x] = 1
        if c == '#': a[y,x] = 2


    if line =='':
        stop = i
        line = lines[i+1]
        num = [c.isnumeric() for c in line]
        codes = []
        while line:
            try:
                n = num.index(False)
                codes.append(int(line[:n]))
                line = line[n:]
                num = num[n:]
                n = num.index(True)
                codes.append((line[:n]))
                line = line[n:]
                num = num[n:]
            except: break
        if len(line):
            if line.isnumeric(): codes.append(int(line))
            else: codes.append(line)
        break

import cv2

p = start
print(start)
print(a)
# print(codes)
print(codes)

'''
print(codes)
dir = 'R'
for code in (codes):
    if isinstance(code,str): dir = code
    else:
        a = np.roll(a, 1)
        print(a)
'''

firstx,lastx = [0]*h,[0]*h
firsty,lasty = [0]*w,[0]*w
for y in range(h):
    for x in range(w):
        if a[y][x] != 0:
            firstx[y] = x
            break
for y in range(h):
    for x in range(w-1,-1,-1):
        if a[y][x] != 0:
            lastx[y] = x
            break
for x in range(w):
    for y in range(h):
        if a[y][x] != 0:
            firsty[x] = y
            break
for x in range(w):
    for y in range(h-1,-1,-1):
        if a[y][x] != 0:
            lasty[x] = y
            break
# print('firstx', firstx)
# print('firsty', firsty)

mapDir = lambda d: (0,1) if d=='R' else (0,-1) if d=='L' else (1,0) if d=='U' else (-1,0)
dirs = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
]
print('wh',w,h)
dirIdx = 0
dir = dirs[dirIdx%4]
for code in (codes):
    if isinstance(code,str):
        assert (code == 'L' or code == 'R')
        dirIdx += 1 if code == 'R' else -1
        if dirIdx >= 4: dirIdx = 0
        if dirIdx<0: dirIdx = 3
        dir = dirs[dirIdx]
    else:
        for i in range(code):
            np = p[0]+dir[0], p[1]+dir[1]

            if np[1] >= w: np = np[0], firstx[np[0]]
            if np[1] <  0: np = np[0], lastx[np[0]]
            if np[0] >= h: np = firsty[np[1]], np[1]
            if np[0] <  0: np = lasty[np[1]], np[1]

            if dir[1] == -1 and a[np[0],np[1]] == 0: np = np[0], lastx[np[0]]
            if dir[1] ==  1 and a[np[0],np[1]] == 0: np = np[0], firstx[np[0]]
            if dir[0] == -1 and a[np[0],np[1]] == 0: np = lasty[np[1]], np[1]
            if dir[0] ==  1 and a[np[0],np[1]] == 0: np = firsty[np[1]], np[1]

            if a[np[0],np[1]] == 2:
                # don't move
                # pass
                break
            else:
                p = np

            if 0:
                print(dir,i,'/',code,p)
                # b = numpy.copy(a)
                # b[p[0],p[1]] = 8
                # print(b)
                # print(b[p[0]-5:p[0]+5, p[1]-5:p[1]+5])
                b = a*100
                b[p[0],p[1]] = 255
                cv2.imshow('a', (b*100).astype(numpy.uint8))
                cv2.waitKey(1)
print((1+p[0])*1000 + (p[1]+1)*4 + (dirIdx))




RIGHT,DOWN,LEFT,UP = dirs



p = start
dirIdx = 0
dir = dirs[dirIdx%4]
for code in (codes):
    if isinstance(code,str):
        assert (code == 'L' or code == 'R')
        dirIdx += 1 if code == 'R' else -1
        if dirIdx >= 4: dirIdx = 0
        if dirIdx<0: dirIdx = 3
        dir = dirs[dirIdx]
    else:
        for i in range(code):

            dd = dir
            nd = dir
            y,x = p
            np = p[0]+dd[0], p[1]+dd[1]

            assert a[p[0],p[1]] == 1

            def getFace(y,x):
                assert y>=0 and y < 200, (y,x)
                assert x>=0 and x < 150, (y,x)
                if y < 50:
                    if x >= 50 and  x < 100: return 1, y, x-50
                    elif x >= 100 and x<150: return 2, y, x-100
                    else: assert False, (y,x)
                elif y < 100:
                    assert x >= 50
                    assert x < 100
                    return 3, y-50, x-50
                elif y < 150:
                    if x < 50: return 4, y-100, x
                    elif x < 100: return 5, y-100, x-50
                    else: assert False
                else:
                    assert y<250
                    assert x<50
                    return 6, y-150, x

            f,ly,lx = getFace(y,x)

            if f == 1 and y == 0 and dd == UP:
                # np = 150 + 49-(x-50), 0
                np = 150 + lx, 0
                nd = RIGHT
                assert getFace(*np)[0] == 6
                print('1 -> 6')
            if f == 1 and x == 50 and dd == LEFT:
                np = 100 + 49-(ly), 0
                nd = RIGHT
                assert getFace(*np)[0] == 4
                print('1 -> 4')

            if f == 2 and y == 0 and dd == UP:
                np = 199, lx
                # nd = DOWN
                nd = UP
                assert getFace(*np)[0] == 6
                print('2 -> 6')
            if f == 2 and x == 149 and dd == RIGHT:
                np = 100+49-ly, 99
                nd = LEFT
                assert getFace(*np)[0] == 5
                print('2 -> 5')
            if f == 2 and y == 49 and dd == DOWN:
                np = 50+lx, 99
                nd = LEFT
                assert getFace(*np)[0] == 3, (np, getFace(*np))
                print('2 -> 3')

            if f == 3 and x == 50 and dd == LEFT:
                nd = DOWN
                np = 100, ly
                assert getFace(*np)[0] == 4
                print('3 -> 4')
            if f == 3 and x == 99 and dd == RIGHT:
                nd = UP
                np = 49, 100 + ly
                assert getFace(*np)[0] == 2
                print('3 -> 2')

            if f == 4 and x == 0 and dd == LEFT:
                nd = RIGHT
                # np = y-100, 50
                np = 49-(ly), 50
                assert getFace(*np)[0] == 1
                print('4 -> 1')
            if f == 4 and y == 100 and dd == UP:
                nd = RIGHT
                np = 50+lx, 50
                assert getFace(*np)[0] == 3
                print('4 -> 3')

            if f == 5 and x == 99 and dd == RIGHT:
                nd = LEFT
                np = 49-(ly), 149
                # np = (ly), 149
                assert getFace(*np)[0] == 2
                print('5 -> 2')
            if f == 5 and y == 149 and dd == DOWN:
                nd = LEFT
                np = 150+lx, 49
                assert getFace(*np)[0] == 6
                print('5 -> 6')

            if f == 6 and x == 0 and dd == LEFT:
                nd = DOWN
                np = 0, 50 + ly
                assert getFace(*np)[0] == 1
                print('6 -> 1')
            if f == 6 and y == 199 and dd == DOWN:
                nd = DOWN
                np = 0, 100 + lx
                assert getFace(*np)[0] == 2
                print('6 -> 2')
            if f == 6 and x == 49 and dd == RIGHT:
                nd = UP
                np = 149, 50 + ly
                assert getFace(*np)[0] == 5
                print('6 -> 5')



            # np = p[0]+dd[0], p[1]+dd[1]

            '''
            if np[1] >= w:
                np = p[0]-100, p[1]-50

            if np[1] <  0: np = np[0], lastx[np[0]]
            if np[0] >= h: np = firsty[np[1]], np[1]
            if np[0] <  0: np = lasty[np[1]], np[1]

            if dd[1] == -1 and a[np[0],np[1]] == 0: np = np[0], lastx[np[0]]
            if dd[1] ==  1 and a[np[0],np[1]] == 0: np = np[0], firstx[np[0]]
            if dd[0] == -1 and a[np[0],np[1]] == 0: np = lasty[np[1]], np[1]
            if dd[0] ==  1 and a[np[0],np[1]] == 0: np = firsty[np[1]], np[1]
            '''

            print(p,np,dir,nd)

            if a[np[0],np[1]] == 2:
                # don't move
                # pass
                break
            else:
                p = np
                while dir != nd:
                    dirIdx += 1
                    if dirIdx >= 4: dirIdx = 0
                    if dirIdx<0: dirIdx = 3
                    dir = dirs[dirIdx]

            if 0:
                # print(dd,i,'/',code,p)
                # b = numpy.copy(a)
                # b[p[0],p[1]] = 8
                # print(b)
                # print(b[p[0]-5:p[0]+5, p[1]-5:p[1]+5])
                b = a*100
                b[p[0],p[1]] = 255
                cv2.imshow('a', (b*100).astype(numpy.uint8))
                cv2.waitKey(100)
print((1+p[0])*1000 + (p[1]+1)*4 + (dirIdx))
