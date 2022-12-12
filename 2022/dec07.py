import sys
from functools import lru_cache

lines = [l[:-1] for l in sys.stdin.readlines()]
dirs = set()

d, st = {}, []
for line in lines:
    if line[:4] == '$ cd':
        act = line[5:]
        if act == '..':
            st.pop()
        else:
            st.append(act)
    elif line[:4] == '$ ls':
        pass

    elif line[:3] == 'dir':
        subdir = line[4:]

        k = '_'.join(st)
        dirs.add(k+'_'+subdir)
        if k not in d: d[k] = []
        d[k].append('_'.join(st+[subdir]))
    else:
        k = '_'.join(st)
        if k not in d: d[k] = []
        d[k].append(int(line.split(' ')[0]))

@lru_cache(1024)
def sum_it(k):
    s = 0
    for v in d[k]:
        if isinstance(v,int): s += v
        # else: s += d['_'.join(v)]
        else: s += sum_it(v)
    return s

acc = 0
for k in d.keys():
    x = sum_it(k)
    if x <= 100000:
        acc += x
print(acc)



N = 70000000
M = 30000000
L = sum_it('/')
A = N - L
print('taken',L,'avail',A)
min,argmin = 9999999999999,0
for k in d.keys():
    if k in dirs:
        x = sum_it(k)
        if k in dirs and A+x >= M and x < min:
            min = x
            argmin = k
print(argmin,min)
