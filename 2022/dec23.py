import sys
# import numpy as np
# import numpy
import re
# lines = [l.strip() for l in sys.stdin.readlines()]
lines = [l[:-1] for l in sys.stdin.readlines()]

G = {(y,x):0 for y,l in enumerate(lines)
             for x,c in enumerate(l) if c == '#'}

if 0:
    loy,lox = min([k[0] for k in G]), min([k[1] for k in G])
    w = max([k[1] for k in G]) - min([k[1] for k in G])
    h = max([k[0] for k in G]) - min([k[0] for k in G])
    a=np.zeros((h+1,w+1), dtype=np.uint8)
    for y,x in G:
        a[y-loy,x-lox] = 1
    print(' - Begin',round)
    print(a)

DIRS = 'NSWE'

# for round in range(10):
for round in range(9910000):
    # P = {p: propose(p, v, G) for p,v in G.items()}
    P = {}
    # print('num',len(G))

    GG = {}
    for (y,x), v in G.items():
        nearby = 0
        for dy in range(-1,2):
            for dx in range(-1,2):
                if dy != 0 or dx != 0:
                    if (y+dy, x+dx) in G:
                        nearby += 1
                        break

        d0 = v

        if nearby == 0:
            # print('skip',y,x)
            GG[(y,x)] = (d0+1)%4
            # GG[(y,x)] = d0
            continue

        # Increment now
        G[y,x] = (d0+1) % 4
        # G[y,x] = d0

        anyvalid = False
        for dd in range(d0,d0+4):
            d = dd % 4

            valid = True
            if DIRS[d] == 'N':
                for dx in range(-1,2):
                    if (y-1,x+dx) in G: valid = False
                if valid:
                    anyvalid = True
                    P[(y,x)] = y-1,x; break

            valid = True
            if DIRS[d] == 'S':
                for dx in range(-1,2):
                    if (y+1,x+dx) in G: valid = False
                if valid:
                    anyvalid = True
                    P[(y,x)] = y+1,x; break

            valid = True
            if DIRS[d] == 'W':
                for dy in range(-1,2):
                    if (y+dy,x-1) in G: valid = False
                if valid:
                    anyvalid = True
                    P[(y,x)] = y,x-1; break

            valid = True
            if DIRS[d] == 'E':
                for dy in range(-1,2):
                    if (y+dy,x+1) in G: valid = False
                if valid:
                    anyvalid = True
                    P[(y,x)] = y,x+1; break

        if not anyvalid:
            # GG[y,x] = d0
            GG[y,x] = (d0+1)%4
            # print(y,x)
            # GG[y,x] = G[y,x]


    # Take any valid proposals and move the eleves
    PP = {}
    for old,new in P.items():
        if new in G:
            assert(False)
        if new in GG:
            assert(False)

        if new in PP:
            # print('blocking', old, new)
            if PP[new] != 'blocked': GG[PP[new]] = G[old]
            GG[old] = G[old]
            PP[new] = 'blocked'
        else:
            PP[new] = old

    for new,old in PP.items():
        if old != 'blocked':
            GG[new] = G[old]
            # del G[old]
        else:
            # print('block')
            pass



    if set(G.keys()) == set(GG.keys()):
        print(' - Stopping on round', round+1)
        break



    G = dict(GG)
    # print('num at line',len(GG))

    if round % 1000 == 0: print('round',round)

    '''
    if 0:
        loy,lox = min([k[0] for k in G]), min([k[1] for k in G])
        w = max([k[1] for k in G]) - min([k[1] for k in G])
        h = max([k[0] for k in G]) - min([k[0] for k in G])
        a=np.zeros((h+1,w+1), dtype=np.uint8)
        for y,x in G:
            a[y-loy,x-lox] = G[y,x]
        print(' - After round',round)
        for r in a:
            for c in r:
                print(c, end='')
            print('')
        # print(a)
    '''


loy,lox = min([k[0] for k in G]), min([k[1] for k in G])
w = 1+max([k[1] for k in G]) - min([k[1] for k in G])
h = 1+max([k[0] for k in G]) - min([k[0] for k in G])
print(w,h)
print(w*h - len(G))
print('num',len(G))

