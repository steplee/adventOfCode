import sys

lines = [l[:-1] for l in sys.stdin.readlines()]
packets = []
for i in range(0,len(lines)//3+1,1):
    packets.append((
        eval(lines[i*3+0]),
        eval(lines[i*3+1])))

def go(ls,rs):
    # print(ls,rs)
    if isinstance(ls, int) and isinstance(rs, int):
        if ls == rs: return 'go'
        if ls < rs: return 'yes'
        if ls > rs: return 'no'
    if isinstance(ls,list) and not isinstance(rs,list): return go(ls,[rs])
    if isinstance(rs,list) and not isinstance(ls,list): return go([ls],rs)
    if len(ls) == 0 and len(rs) != 0: return 'yes'
    if len(rs) == 0 and len(ls) != 0: return 'no'
    for l,r in zip(ls,rs):
        o = go(l,r)
        # print('---',l,r,o)
        if o != 'go': return o
    if len(ls) == len(rs): return 'go'
    return 'yes' if len(ls) <= len(rs) else 'no'

acc = 0
for i,pair in enumerate(packets):
    # print(' -------------------------------',i)
    v = int(go(*pair) == 'yes')
    # print(i,'->',v)
    acc += (i+1) * v
print(acc)

# python's "sorted" does not allow binary comparison (unlike C++'s)
# so just write a selection sort...
def selection_sort(xs):
    out = []
    while len(xs):
        besti,best = 0,xs[0]
        for i,x in enumerate(xs[1:]):
            if go(best, x) == 'no':
                besti,best = i+1, x
        out.append(xs.pop(besti))
    return out


packets.append(([[2]], [[6]]))
flatPackets = []
for p in packets: flatPackets.extend(p)

# for a in (selection_sort(flatPackets)): print(a)
y = selection_sort(flatPackets)
print((1+y.index([[2]])) * (1+y.index([[6]])))
