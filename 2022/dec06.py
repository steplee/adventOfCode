import sys

line = [l[:-1] for l in sys.stdin.readlines()][0]

for i in range(4, len(line)):
    s = line[i-4:i]
    if len(set(s)) == len(s):
        print(i)
        break

for i in range(14, len(line)):
    s = line[i-14:i]
    if len(set(s)) == len(s):
        print(i)
        break
