import sys
from copy import deepcopy
lines = [l[:-1] for l in sys.stdin.readlines()]

import re
coords = [[int(a) for a in re.findall('=([-\d]+)', l)] for l in lines]
S = [c[:2] for c in coords]
B = [c[2:] for c in coords]

# y = 10
y = 2000000

if 0:
    seen = set([])
    for s,b in zip(S,B):
        d = (abs(s[0]-b[0]) + abs(s[1]-b[1]))

        dsy = abs(s[1] - y)

        dx = (d - dsy)
        if dx > 0:
            # print(dx)
            for xx in range(s[0]-dx, s[0]+dx):
                seen.add(xx)

    print(len(seen))


#
# My idea is to walk one cell beyond the blocked diamond
# from each sensor.
# Visting each cell, check if ANY beacon can see it.
#
# Any cell that has NO beacons that see is the answer.
# And conversely, the beacon MUST be one away from the blocked area.
#
# This will work, but takes a few minutes to run on my i7.
# I guess there is a more efficient solution...

M = 4000000
# M = 20

import numpy as np
SS = np.array(S)
BB = np.array(B)
DD = abs(SS-BB).sum(1)

for i,(s,b) in enumerate(zip(S,B)):

    d = (abs(s[0]-b[0]) + abs(s[1]-b[1]))
    print(i,'/',len(S))

    xx,yy = s[0] - (d+1), s[1]

    def check(xx,yy):
        dd = abs(SS - (xx,yy)).sum(1)
        dd = dd <= DD
        # print(dd)
        if not dd.any():
            print('found it!!!!!', xx,yy)
            print(xx*4000000+yy)
            sys.exit(0)

    while xx != s[0]:
        xx,yy = xx+1, yy+1
        if xx>0 and yy>0 and xx<=M and yy<=M: check(xx,yy)
    while yy != s[1]:
        xx,yy = xx+1, yy-1
        if xx>0 and yy>0 and xx<=M and yy<=M: check(xx,yy)
    while xx != s[0]:
        xx,yy = xx-1, yy-1
        if xx>0 and yy>0 and xx<=M and yy<=M: check(xx,yy)
    while yy != s[1]:
        xx,yy = xx-1, yy+1
        if xx>0 and yy>0 and xx<=M and yy<=M: check(xx,yy)


