import sys

lines = [l[:-1] for l in sys.stdin.readlines()]
grid = [[ord(a) - ord('a') for a in line] for line in lines]
H,W = len(grid), len(grid[0])

for y in range(H):
    for x in range(W):
        if grid[y][x] == ord('S')-ord('a'):
            s = (x,y)
            grid[y][x] = ord('a')
        if grid[y][x] == ord('E')-ord('a'):
            t = (x,y)
            grid[y][x] = ord('z')-ord('a')

pred,cost = {}, {}

st = [(s,0)]

while st:
    (x,y), c = st.pop()
    v = grid[y][x]

    for dxy in ((-1,0), (1,0), (0,-1), (0,1)):
        pp = x+dxy[0], y+dxy[1]
        if pp[0] >= 0 and pp[0] < W and pp[1] >= 0 and pp[1] < H:
            if grid[pp[1]][pp[0]] <= v+1:
                cc = c+1
                if pp not in cost:
                    cost[pp] = cc
                    st.append((pp,cc))
                elif cc < cost[pp]:
                    cost[pp] = cc
                    st.append((pp,cc))
print(cost[t])



# Part 2, same thing but start with more states, and
# make sure to record all of there initial costs

st = []
for y in range(H):
    for x in range(W):
        if grid[y][x] == 0:
            st.append(((x,y), 0))
for p,c in st:
    cost[p] = c

while st:
    (x,y), c = st.pop()
    v = grid[y][x]

    for dxy in ((-1,0), (1,0), (0,-1), (0,1)):
        pp = x+dxy[0], y+dxy[1]
        if pp[0] >= 0 and pp[0] < W and pp[1] >= 0 and pp[1] < H:
            if grid[pp[1]][pp[0]] <= v+1:
                cc = c+1
                if pp not in cost:
                    cost[pp] = cc
                    st.append((pp,cc))
                elif cc < cost[pp]:
                    cost[pp] = cc
                    st.append((pp,cc))
print(cost[t])
