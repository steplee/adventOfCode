import sys

lines = [line.strip() for line in sys.stdin.readlines()]

S = {}
E = {}

for line in lines:
    a,b,c = [int(a) for a in line.split(',')]
    S[a,b,c] = 0

cnt =0

for line in lines:
    x,y,z = [int(a) for a in line.split(',')]

    # for dx in range(-1,2):
        # for dy in range(-1,2):
            # for dz in range(-1,2):
                # pass

    for d in range(-1,2):
        if (x+d,y,z) not in S:
                cnt += 1
                E[x+d,y,z] = d
    for d in range(-1,2):
        if (x,y+d,z) not in S:
                cnt += 1
                E[x,y+d,z] = d
    for d in range(-1,2):
        if (x,y,z+d) not in S:
                cnt += 1
                E[x,y,z+d] = d

print(cnt)
cnt = 0

from collections import defaultdict
# O = {}
O = defaultdict(lambda: False)

'''
for line in lines:
    x,y,z = [int(a) for a in line.split(',')]

    good=True
    for d in range(-1,2,2):
        if (x+d,y,z) not in S:
            for i in range(1,100):
                if (x+i*d,y,z) in S:
                    good=False
                    break
            # if good: cnt += 1
            O[x+d,y,z] = good
    good=True
    for d in range(-1,2,2):
        if (x,y+d,z) not in S:
            for i in range(1,100):
                if (x,i*d+y,z) in S:
                    good=False
                    break
            # if good: cnt += 1
            O[x+d,y,z] = good
    good=True
    for d in range(-1,2,2):
        if (x,y,z+d) not in S:
            for i in range(1,100):
                if (x,y,i*d+z) in S:
                    good=False
                    break
            # if good: cnt += 1
            O[x+d,y,z] = good

for line in lines:
    x,y,z = [int(a) for a in line.split(',')]

    good=True
    for d in range(-1,2,2):
        if (x+d,y,z) not in S:
            for i in range(1,100):
                if (x+i*d,y,z) in S:
                    good=O[x+i*d,y,z]
                    break
            if good: cnt += 1
    good=True
    for d in range(-1,2,2):
        if (x,y+d,z) not in S:
            for i in range(1,100):
                if (x,i*d+y,z) in S:
                    good=O[x,y+i*d,z]
                    break
            if good: cnt += 1
    good=True
    for d in range(-1,2,2):
        if (x,y,z+d) not in S:
            for i in range(1,100):
                if (x,y,i*d+z) in S:
                    good=O[x,y,z+i*d]
                    break
            if good: cnt += 1
'''

block = {}
def dfs(x,y,z):
    st = [(x,y,z)]
    all = set()

    while len(st) > 0:

        x,y,z = st.pop()

        if (x,y,z) in block: return block[(x,y,z)]
        all.add((x,y,z))

        for d in range(-1,2):
            if (x+d,y,z) not in S and (x+d,y,z) not in all:
                if abs(x+d) + abs(y) + abs(z) > 40:
                    for a in all: block[a] = 1
                    return 1
                st.append((x+d,y,z))
        for d in range(-1,2):
            if (x,y+d,z) not in S and (x,y+d,z) not in all:
                if abs(x) + abs(y+d) + abs(z) > 40:
                    for a in all: block[a] = 1
                    return 1
                st.append((x,y+d,z))
        for d in range(-1,2):
            if (x,y,z+d) not in S and (x,y,d+z) not in all:
                if abs(x) + abs(y) + abs(z+d) > 40:
                    for a in all: block[a] = 1
                    return 1
                st.append((x,y,z+d))


    for a in all: block[a] = 0
    return 0

for line in lines:
    x,y,z = [int(a) for a in line.split(',')]


    for d in range(-1,2):
        if (x+d,y,z) not in S:
                cnt += dfs(x+d,y,z)
    for d in range(-1,2):
        if (x,y+d,z) not in S:
                cnt += dfs(x,d+y,z)
    for d in range(-1,2):
        if (x,y,z+d) not in S:
                cnt += dfs(x,y,d+z)



print(cnt)
