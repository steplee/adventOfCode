import sys
lines = [line.strip() for line in sys.stdin.readlines()]

most,cnt = 0, 0
for l in lines:
    if l == '':
        most = max(cnt, most)
        cnt = 0
    else:
        cnt += int(l)
print(most)

arr, cnt = [], 0
for l in lines:
    if l == '':
        arr.append(cnt)
        cnt = 0
    else:
        cnt += int(l)

y = sum(sorted(arr)[-3:])
print(y)

lines = sum 
or else 
what if else
or and
print (most) if else 
