import sys

lines = [l[:-1] for l in sys.stdin.readlines()]


stacks = [[] for _ in range(9)]
parseTop = True
for line in lines:

    if len(line) > 0 and line[1] == '1':
        parseTop = False
        stacks = [st[::-1] for st in stacks]

    if parseTop:
        for i,j in enumerate(range(1,34,4)):
            if j < len(line) and line[j] != ' ':
                stacks[i].append(line[j])

    if len(line)>0 and line[0] == 'm':
        _,n,_,fro,_,to = line.split(' ')
        n,fro,to = (int(a) for a in (n,fro,to))

        for i in range(n):
            stacks[to-1].append(stacks[fro-1].pop())
print(''.join([st[-1] for st in stacks]))





stacks = [[] for _ in range(9)]
parseTop = True
for line in lines:

    if len(line) > 0 and line[1] == '1':
        parseTop = False
        stacks = [st[::-1] for st in stacks]

    if parseTop:
        for i,j in enumerate(range(1,34,4)):
            if j < len(line) and line[j] != ' ':
                stacks[i].append(line[j])

    if len(line)>0 and line[0] == 'm':
        _,n,_,fro,_,to = line.split(' ')
        n,fro,to = (int(a) for a in (n,fro,to))

        stacks[to-1].extend(stacks[fro-1][-n:])
        stacks[fro-1] = stacks[fro-1][:-n]
print(''.join([st[-1] for st in stacks]))

