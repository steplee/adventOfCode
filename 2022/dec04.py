import sys

lines = [l.strip() for l in sys.stdin.readlines()]

cnt = 0
for line in lines:
    (a,b), (c,d) = [map(int,s.split('-')) for s in line.split(',')]
    if (a>=c and b<=d) or (c>=a and d<=b):
        print(line,'->','yes')
        cnt += 1
    else:
        print(line,'->','no')
print(cnt,'/', len(lines))

cnt = 0
for line in lines:
    (a,b), (c,d) = [map(int,s.split('-')) for s in line.split(',')]
    if (c <= b and d >= a) or (b <= c and a >= d):
        print(line,'->','yes')
        cnt += 1
    else:
        print(line,'->','no')
print(cnt,'/', len(lines))
