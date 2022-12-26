import sys
import re
lines = [l.strip() for l in sys.stdin.readlines()]

d = {}
rem = []
mapp = {}
for line in lines:
    m,z = line.split(':')
    if '+' in z or '-' in z or '*' in z or '/' in z:
        a,op,b = z.strip().split(' ')
        rem.append((m,a,op,b))
        mapp[m] = (a,op,b)
    else: d[m] = int(z.strip())

while len(rem):
    rem2 = []
    for (m, a,op,b) in rem:
        if a in d and b in d:
            aa,bb = d[a], d[b]
            d[m] = (aa+bb) if op == '+' else (aa*bb) if op == '*' else (aa//bb) if op == '/' else aa-bb
        else:
            rem2.append((m,a,op,b))
    rem = rem2

print('part1 answer', d['root'])

# DFS, with the recursion stopping when:
#         we hit a constant, in which case we return False.
#         we hit a humn, in which case we return the answer
# Otherwise, recurse two branches, setting the target with the corrected
# algebra modified with the operation and inputs to this node.
def dfs(curr, target):
    if curr == 'humn':
        return target

    if curr in mapp:
        a,op,b = mapp[curr]

        aa,bb = d[a], d[b]

        # print(curr,target, op,aa,bb)

        # stupid algebra held me up for way too long...
        if op == '*': l = target // bb
        if op == '+': l = target - bb
        if op == '/': l = bb * target
        if op == '-': l = bb + target

        if op == '*': r = target // aa
        if op == '+': r = target - aa
        if op == '/': r = aa // target
        if op == '-': r = aa - target

        if ra := dfs(a,l) is not None:
            return ra
        rb = dfs(b, r)
        if rb is not None:
            return rb

    else:
        return None # We hit a non-'humn' constant

# Exactly one of these will fail (return None)
# The other is the answer
print('part2 answer')
print(dfs(mapp['root'][0], d[mapp['root'][2]]))
print(dfs(mapp['root'][2], d[mapp['root'][0]]))
