import sys
from copy import deepcopy
lines = [l[:-1] for l in sys.stdin.readlines()]

minx, maxx, maxy = 499, 501, 1

occ = {}
endPerColumn = {}
for line in lines:
    parts = line.split(' -> ')
    pts = []
    for part in parts:
        x,y = part.split(',')
        pts.append((int(x),int(y)))
    for i in range(1,len(pts)):
        prev = pts[i-1]
        curr = pts[i]
        if prev[0] == curr[0]: # is vertical
            for y in range(min(prev[1],curr[1]), 1+max(prev[1],curr[1])):
                occ[(prev[0],y)] = 1
                if prev[0] not in endPerColumn or endPerColumn[prev[0]] < y: endPerColumn[prev[0]] = y
        elif prev[1] == curr[1]: # is horiz
            for x in range(min(prev[0],curr[0]), 1+max(prev[0],curr[0])):
                occ[(x,prev[1])] = 1
                if x not in endPerColumn or endPerColumn[x] < prev[1]: endPerColumn[x] = prev[1]
        else: assert False

def print_(o):
    print(' - Grid:')
    grid = [[0]*32 for _ in range(12)]
    for (x,y) in o.keys():
        grid[y][x-500+16] = 1
    for r in grid: print(''.join([' ' if c == 0 else '#' for c in r]))

stop = False
cnt = 0
occ1 = deepcopy(occ)
while not stop:
    x,y = (500, 1)
    while True:
        if occ1.get((x,y+1), 0) == 0:
            y = y+1

            if x not in endPerColumn or y > endPerColumn[x]:
                stop = True
                break

        elif occ1.get((x-1,y+1), 0) == 0:
            x,y = x-1,y+1
        elif occ1.get((x+1,y+1), 0) == 0:
            x,y = x+1,y+1
        else:
            occ1[(x,y)] = 1
            cnt += 1
            break
# print_(occ1)
print(cnt)




# Part 2

max_y = max(endPerColumn.values()) + 1
print(max_y)

stop = False
cnt = 0
occ1 = deepcopy(occ)
while not stop:
    x,y = (500, 0)
    while True:

        if y >= max_y:
            if occ1.get((x,y),0) == 0:
                occ1[(x,y)] = 1
                cnt += 1
                break
            else:
                stop = True
                break

        elif occ1.get((x,y+1), 0) == 0:
            y = y+1

            # if x not in endPerColumn or y > endPerColumn[x]:
            # if y > max_y+1:
                # stop = True
                # break

        elif occ1.get((x-1,y+1), 0) == 0:
            x,y = x-1,y+1
        elif occ1.get((x+1,y+1), 0) == 0:
            x,y = x+1,y+1
        else:
            if occ1.get((x,y),0) == 0:
                occ1[(x,y)] = 1
                cnt += 1
                break
            else:
                stop = True
                break
# print_(occ1)
print(cnt)
