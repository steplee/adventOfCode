import sys
import numpy as np
np.set_printoptions(linewidth=200, edgeitems=20)

# jet = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
jet = sys.stdin.readlines()[0][:-1]
jet = [1 if j == '>' else -1 for j in jet]
# jet = jet * (1 + (1+2022) // len(jet))

shapes = [
        np.array([1,1,1,1], dtype=np.uint8).reshape(1,4),
        np.array([0,1,0,1,1,1,0,1,0], dtype=np.uint8).reshape(-1,3),
        np.array([0,0,1, 0,0,1, 1,1,1], dtype=np.uint8).reshape(-1,3),
        np.array([1,1,1,1], dtype=np.uint8).reshape(4,1),
        np.array([1,1,1,1], dtype=np.uint8).reshape(2,2)
]


# This would take 30 minutes, lol. Even in c++ it would take forever.
# That suggests there is a way to find a certain pattern and multiply to get answer...
'''
from tqdm import tqdm
for i in tqdm(range(1000000000000)):
    pass
'''

def part1():

    occ = np.zeros((2022*4+10, 7), dtype=np.uint8)
    topy = occ.shape[0]
    ji = 0
    print('start topy', topy)

    for i in range(2022):
    # for i in range(1000000000000):
    # for i in range(12):
    # for i in range(10):
        shape = shapes[i%5]
        # layer = np.zeros((shape.shape[0], 7), dtype=np.uint8)

        H,W = shape.shape
        x,y = 2, topy-H-3

        while True:
            if 0:
                print(' - i',i, 'xy', x, y, 'topy', topy)
                occ1 = np.copy(occ)
                occ1[y:y+H,x:x+W] |= shape*2
                print(occ1[-8:])


            move = jet[ji%len(jet)]
            ji += 1
            nx = x + move


            if not (nx + W <= 7 and nx >= 0):
                # print('not moving', x, nx, move)
                pass
            elif ((occ[y:y+H, nx:nx+W] * shape) == 1).any():
                # print('not moving', x, nx, move)
                pass
            else:
                # print('moving', x, nx, move)
                x = nx

            if y+H == occ.shape[0] or ((occ[y:y+H, x:x+W] * shape) == 1).any():
                occ[y:y+H, x:x+W] |= shape
                topy = min(topy,y)
                break

            if ((occ[y+1:y+1+H, x:x+W] * shape) == 1).any():
                # print(' - stopping2 ahead of y',y)
                occ[y:y+H, x:x+W] |= shape
                topy = min(topy,y)
                break

            if y+H == occ.shape[0] or ((occ[y:y+H, x:x+W] * shape) == 1).any():
                # print(' - stopping3 ahead of y',y)
                occ[y:y+H, x:x+W] |= shape
                topy = min(topy,y)
                break
            y = y + 1
    # print(occ[-20:])
    print('final topy', topy)
    print(occ.shape[0]-topy)

def part2_attempt1():
    '''
    My idea is to find the first time that the current state looks like the first state.
    That would happen when jet & shape indices are zero and the top-most level is full.
    '''

    occ = np.zeros(((1024*1024*8)*4+10, 7), dtype=np.uint8)
    topy = occ.shape[0]
    ji = 0
    print('start topy', topy)

    d = {}
    out = 0
    PHASE = 0
    firstHit = 0
    target = -1
    hd = {} # heights at states

    occSave = None
    topySave = None

    i = 0
    N = 1000000000000
    # N = 2022
    while i < N:
    # for i in range(10):
        shape = shapes[i%5]
        # print(i)

        # print(topy/occ.shape[0])

        H,W = shape.shape
        x,y = 2, topy-H-3

        if topy < 0:
            print(' - ran out of space.')
            break

        # How far top block is from topy
        l = [occ.shape[0]-topy]*7
        for col in range(7):
            for yy in range(topy, occ.shape[0]):
                if occ[yy,col] != 0:
                    l[col] = yy-topy
                    break
        # print('l',l,'topy',topy)
        # print(occ[topy-1:])

        if PHASE == 0:
            k = (i%5,ji,*l)
            hd[i] = topy


            if k in d:
            # if k in d and d[k] == 0:
                print(' - (0) FOUND MATCHING STATE', i, '->', d[k])
                # print(occ[topy:topy+10])
                PHASE = 1
                target = d[k]
                firstHit = i
                # out += occ.shape[0]-topy
                occSave = np.copy(occ)
                topySave = topy
                # break
            else:
                d[k] = i

        elif PHASE == 1:
            k = (i%5,ji,*l)
            hd[i] = topy

            if k in d and d[k] == target:
                print(' - (1) FOUND MATCHING STATE', i, '->', d[k])
                PHASE = 2
                n = ((N-i) // (i - firstHit))
                oi = i

                print('mult',(hd[firstHit]-hd[oi])*n)
                print('out',out)

                out += -(hd[i] - hd[firstHit]) * (n)
                # out += -(hd[i] - hd[firstHit]) * (n+1)

                # out += -(-35) * (n+1)
                # i += n * (i-firstHit)
                i = firstHit + (n) * (i-firstHit)
                print(' -> skip to',i, 'n', n, 'diff', hd[oi]-hd[firstHit])
                print(' -> new out', out)


                '''
                occ[:] = 0
                topy = occ.shape[0]-max(l)
                print('reset topy',occ.shape[0]-topy)
                for iii,ll in enumerate(l):
                    if topy+ll < occ.shape[0]:
                        occ[topy+ll,iii] = 1
                print('- RESET')
                print(occ[topy:])
                '''

                occ = np.copy(occSave)
                topy = topySave
                continue



        while True:
            if 0:
                print(' - i',i, 'xy', x, y, 'topy', topy)
                occ1 = np.copy(occ)
                occ1[y:y+H,x:x+W] |= shape*2
                print(occ1[-8:])


            move = jet[ji]
            ji += 1
            if ji >= len(jet): ji = 0
            nx = x + move


            if not (nx + W <= 7 and nx >= 0):
                pass
            elif ((occ[y:y+H, nx:nx+W] * shape) == 1).any():
                pass
            else:
                x = nx

            if y+H == occ.shape[0] or ((occ[y:y+H, x:x+W] * shape) == 1).any():
                occ[y:y+H, x:x+W] |= shape
                topy = min(topy,y)
                break

            if ((occ[y+1:y+1+H, x:x+W] * shape) == 1).any():
                # print(' - stopping2 ahead of y',y)
                occ[y:y+H, x:x+W] |= shape
                topy = min(topy,y)
                break

            if y+H == occ.shape[0] or ((occ[y:y+H, x:x+W] * shape) == 1).any():
                # print(' - stopping3 ahead of y',y)
                occ[y:y+H, x:x+W] |= shape
                topy = min(topy,y)
                break
            y = y + 1
        i = i+1

    out += occ.shape[0]-topy

    # print(occ[-20:])
    # print('final topy', topy)
    # print(occ.shape[0]-topy)
    print(out)

part1()
part2_attempt1()
