import sys

def map(c):
    if c >= 'A' and c <= 'Z': return ord(c) - ord('A') + 26 + 1
    if c >= 'a' and c <= 'z': return ord(c) - ord('a') + 1
    assert False

out = 0

lines = [line.strip() for line in sys.stdin.readlines()]

for line in lines:
    n = len(line)
    a,b = line[:n//2], line[n//2:]
    a = set([map(c) for c in a])
    b = set([map(c) for c in b])
    for u in a:
        if u in b:
            out += u

print(out)

out2 = 0
for i in range(len(lines)//3):
    a,b,c = lines[i*3+0], lines[i*3+1], lines[i*3+2]
    a,b,c = set(a),set(b),set(c)


    lst = []
    for u in a:
        if u in b and u in c:
            out2 += map(u)
            lst.append(u)
    assert len(lst) == 1
print(out2)
