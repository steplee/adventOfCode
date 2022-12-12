import sys


lines = list(sys.stdin.readlines())

acc = 0
for line in lines:
    u,v = 1+ord(line[0])-ord('A'), 1+ord(line[2])-ord('X')
    acc0 = v
    if u == v: acc0 += 3
    # rock beats scissor, paper beats rock, scissor beats paper
    elif (v == 1 and u == 3) or (v == 2 and u == 1) or (v == 3 and u == 2): acc0 += 6
    acc += acc0
    # print(u,v,'->',acc0)

print(acc)

acc = 0
for line in lines:
    u,R = 1+ord(line[0])-ord('A'), 1+ord(line[2])-ord('X')

    acc0 = 0

    if R == 1: # lose
        v = 3 if u == 1 else (1 if u == 2 else 2)
    elif R == 2: # tie
        v = u
    else: # win
        v = 1 if u == 3 else (2 if u == 1 else 3)

    acc0 += v
    if u == v: acc0 += 3
    elif (v == 1 and u == 3) or (v == 2 and u == 1) or (v == 3 and u == 2): acc0 += 6
    acc += acc0
    # print(u,v,'->',acc0,acc)

print(acc)
