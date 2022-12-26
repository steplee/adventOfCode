import sys
from copy import deepcopy
lines = [line.strip() for line in sys.stdin.readlines()]

S = (0,1)
T = len(lines)-1, len(lines[0])-2

# G = {}
h,w = len(lines) , len(lines[0])
G = [[None for _ in range(w)] for _ in range(h)]
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        G[y][x] = [c]
OG = deepcopy(G)

def printIt(G):
    print(G)
    for l in G:
        # print(l)
        l = [str(len(l)) if len(l) > 1 else l[0] for l in l]
        print(''.join(l))


def step(G):
    GG = [[None for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            g = []
            if y == 0 or y == h-1 or x == 0 or x == w-1:
                g = G[y][x]
            else:
                for dy in (-1,1):
                    if y == 1 and dy == -1:
                        for c in G[h-2][x]:
                            if c == 'v':
                                g.append(c)

                    elif y == h-2 and dy ==  1:
                        for c in G[1][x]:
                            if c == '^':
                                g.append(c)

                    else:
                        # for c in G[y+dy][x][i] == 'v' and dy == -1) or (dy ==  1 and G[y+dy][x][i] == '^'):
                        for c in G[y+dy][x]:
                            if dy == -1 and c == 'v':
                                g.append(c)
                            if dy ==  1 and c == '^':
                                g.append(c)

                for dx in (-1,1):
                    if x == 1 and dx == -1:
                        for c in G[y][w-2]:
                            if c == '>':
                                g.append(c)

                    elif x == w-2 and dx ==  1:
                        for c in G[y][1]:
                            if c == '<':
                                g.append(c)

                    else:
                        # if (G[y][x+dx] == '<' and dx == 1) or (dx == -1 and G[y][x+dx] == '>'):
                            # g.append(G[y][x+dx][i])
                        for c in G[y][x+dx]:
                            if dx == -1 and c == '>':
                                g.append(c)
                            if dx ==  1 and c == '<':
                                g.append(c)

            if len(g) == 0: g = ['.']
            GG[y][x] = g
    return GG


# O = [[]*w for _ in range(h)]
O = {(0,1): 0}
print(O)

for t in range(2000):
    stop = False
    G = step(G)
    OO = {}
    # printIt(G)

    for (y,x),v in O.items():
        for dy in range(-1,2):
            for dx in range(-1,2):
                if dx == 0 or dy == 0:
                    yy,xx = dy + y, dx + x
                    if (yy,xx) == T:
                        print(' - found', 1+t)
                        stop = True
                        break
                    if (yy,xx) == S:
                        OO[yy,xx] = t
                    if yy>0 and yy<h-1 and xx>0 and xx<w-1:
                        if G[yy][xx] == ['.']:
                            OO[yy,xx] = t
    if stop:
        break

    O = OO
    print(O)






O = {(0,1): 0}
print(O)
stage = 0
G = deepcopy(OG)

for t in range(3470):
    stop = False
    justGotStage1 = False
    justGotStage2 = False
    G = step(G)
    OO = {}
    # printIt(G)

    for (y,x),v in O.items():
        for dy in range(-1,2):
            for dx in range(-1,2):
                if dx == 0 or dy == 0:
                    yy,xx = dy + y, dx + x
                    if (yy,xx) == T:
                        if stage == 0:
                            stage = 1
                            justGotStage1 = True
                        if stage == 2:
                            print(' - found', 1+t)
                            stop = True
                            break
                    if (yy,xx) == S:
                        if stage == 0:
                            OO[yy,xx] = t
                        elif stage == 1:
                            stage = 2
                            justGotStage2 = True
                    if yy>=0 and yy<h and xx>=0 and xx<w:
                        if G[yy][xx] == ['.']:
                            OO[yy,xx] = t
    if stop:
        break
    if justGotStage1:
        OO = {T: 1}
        print('stage 1',OO)
    if justGotStage2:
        OO = {S: 1}
        print('stage 2',OO)

    O = OO
    print(O)
