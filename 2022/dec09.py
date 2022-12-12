import sys
from copy import deepcopy

lines = [l[:-1] for l in sys.stdin.readlines()]

grid = {}

h,t = (0,0), (0,0)

dirs = dict(U=(1,0), D=(-1,0), R=(0,1), L=(0,-1))


for line in lines:
    d,n = line.split(' ')
    n = int(n)
    for i in range(n):
        h = (h[0]+dirs[d][0], h[1]+dirs[d][1])

        dif = \
            max(-1,min(1,h[0] - t[0])), \
            max(-1,min(1,h[1] - t[1]))

        dt = dif
        if abs(h[0]-t[0]) >= 2 or abs(h[1]-t[1]) >= 2 or (
            (abs(h[0]-t[0]) + abs(h[1]-t[1])) >= 2 and
            (abs(h[0]-t[0]) != abs(h[1]-t[1]))):
                t = (t[0]+dt[0], t[1]+dt[1])

        # print(h,t)
        grid[t] = 1

        '''
        grid1 = [[0 for _ in range(6)] for _ in range(6)]
        grid1[t[0]][t[1]] = 'T'
        grid1[h[0]][h[1]] = 'H'

        for a in grid1[::-1]:
            print(a)
        print('')
        '''
print(len(grid))

grid = {}

P = {k:(0,0) for k in range(10)}

for line in lines:
    d,n = line.split(' ')
    n = int(n)
    for i in range(n):

        P[0] = (P[0][0]+dirs[d][0], P[0][1]+dirs[d][1])

        for j in range(1,10):

            dif = \
                max(-1,min(1,P[j-1][0] - P[j][0])), \
                max(-1,min(1,P[j-1][1] - P[j][1]))

            dt = dif
            if abs(P[j-1][0]-P[j][0]) >= 2 or abs(P[j-1][1]-P[j][1]) >= 2 or (
                (abs(P[j-1][0]-P[j][0]) + abs(P[j-1][1]-P[j][1])) >= 2 and
                (abs(P[j-1][0]-P[j][0]) != abs(P[j-1][1]-P[j][1]))):
                    P[j] = (P[j][0]+dt[0], P[j][1]+dt[1])

        grid[P[9]] = 1
print(len(grid))
