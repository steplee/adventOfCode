import sys

lines = [l[:-1] for l in sys.stdin.readlines()]

clk = 0
x = 1
state = []
state.append((clk,x))

for line in lines:
    if 'addx' in line:
        clk += 2
        state.append((clk,x))
        x += int(line.split(' ')[1])
    else:
        clk += 1
        state.append((clk,x))

prevc = 0
acc = 0
CC =(20,60,100,140,180,220)
CCi = 0
for c,v in state:
    if prevc < CC[CCi] and c >= CC[CCi]:
        print(c,CC[CCi],v)
        acc += CC[CCi] * v
        CCi += 1
        if CCi >= len(CC): break
    prevc = c
print(acc)


statei = 0
for y in range(6):
    row = [' '] * 40
    for x in range(40):
        clk = y*40+x
        while state[statei][0] <= clk:
            statei += 1
        xx = state[statei][1]
        if xx >= x-1 and xx <= x+1:
            row[x] = '#'
    print(''.join(row))
