import sys
from copy import deepcopy
import numpy as np

lines = [[int(a) for a in l[:-1]] for l in sys.stdin.readlines()]

h,w = len(lines), len(lines[0])
reach = [[0] * w for _ in range(h)]

# left -> right
pre = deepcopy(lines)
for y in range(h):
    for x in range(1,w):
        if lines[y][x] > pre[y][x-1]: reach[y][x] = 1
        pre[y][x] = max(pre[y][x-1], lines[y][x])

# right -> left
pre = deepcopy(lines)
for y in range(h):
    for x in range(w-2,-1,-1):
        if lines[y][x] > pre[y][x+1]: reach[y][x] = 1
        pre[y][x] = max(pre[y][x+1], lines[y][x])

# down -> up
pre = deepcopy(lines)
for y in range(1,h):
    for x in range(w):
        if lines[y][x] > pre[y-1][x]: reach[y][x] = 1
        pre[y][x] = max(pre[y-1][x], lines[y][x])

# up -> down
pre = deepcopy(lines)
for y in range(h-2,-1,-1):
    for x in range(w):
        if lines[y][x] > pre[y+1][x]: reach[y][x] = 1
        pre[y][x] = max(pre[y+1][x], lines[y][x])

# Final
out = 2*(h-2) + 2*w
# out = 0
for y in range(1,h-1):
    for x in range(1,w-1):
        # if lines[y][x] > pre[y][x]: out += 1
        if reach[y][x]: out+=1
print(out,'/',w*h)




best = 0
for y in range(1,h-1):
    for x in range(1,w-1):
        if reach[y][x]:
            score = [1] * 4
            me = lines[y][x]
            for yy in range(y+1,h-1):
                if lines[yy][x] < me: score[0] += 1
                else: break
            for yy in range(y-1,0,-1):
                # print(lines[yy][x], 'vs', me)
                if lines[yy][x] < me: score[1] += 1
                else: break
            for xx in range(x+1,w-1):
                if lines[y][xx] < me: score[2] += 1
                else: break
            for xx in range(x-1,0,-1):
                if lines[y][xx] < me: score[3] += 1
                else: break
            best = max(best,np.prod(score))
print(best)

