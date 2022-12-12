import sys
import math
lines = [l[:-1] for l in sys.stdin.readlines()]

monkeys = []
i = 0
while 1:
    i += 1
    it = [int(a) for a in lines[i].split(':')[1].replace(',','').split(' ') if len(a)>0]
    i += 1
    op = lines[i].split(' ')[-2:]
    op = (op[0], op[1])
    i += 1
    test = int(lines[i].split(' ')[-1])
    i += 1
    to = int(lines[i].split(' ')[-1])
    i += 1
    fro = int(lines[i].split(' ')[-1])
    i += 1
    i += 1
    monkeys.append((it,op,test,to,fro))
    if i >= len(lines): break
# print(monkeys)

#modulus = (13*19*23*17)
modulus = 1
for m in monkeys:
    modulus *= m[2]

monkeyCnt = [0] * len(monkeys)
for r in range(10000):
    # if r % 100 == 0: print(r)
    for mi, m in enumerate(monkeys):
        for k in m[0]:
            monkeyCnt[mi] += 1
            kk=k
            other = int(k) if m[1][1] == 'old' else int(m[1][1])
            if m[1][1] == 'old':
                # k = (k%modulus) * (k%modulus)
                k = (k*k) % modulus
            else:
                if m[1][0] == '*': k = (other * k)
                else: k = other + k
            # print(kk, m[1], '->',k)
            if k % m[2] == 0:
                monkeys[m[3]][0].append(k)
            else:
                monkeys[m[4]][0].append(k)
        while m[0]: m[0].pop()

monkeyCnt = sorted(monkeyCnt)
print(monkeyCnt)
print(monkeyCnt[-1]*monkeyCnt[-2])
