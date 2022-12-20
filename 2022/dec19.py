import sys
import re
lines = [l.strip() for l in sys.stdin.readlines()]

# See below for key to keeping number of states manageable.
# Also: run this with pypy!

B = []
for line in lines:
    b,oreOre,clayOre, obsOre,obsClay, geodeOre, geodeObs  = [int(i) for i in re.findall('(\d+)', line)]
    it =  [int(i) for i in re.findall('(\d+)', line)]
    B.append(it)

def solveOne(b,oreOre,clayOre, obsOre,obsClay, geodeOre, geodeObs, T=24):
    M = {}

    # ore clay obs geode
    bots = [1, 0, 0, 0]
    res  = [0, 0, 0]
    st = bots + res

    # HASH = lambda a: '_'.join(map(str,a))
    HASH = lambda a: tuple(a)

    threads = {HASH(st): 0}

    MO = max([oreOre, clayOre, geodeOre, obsOre])

    for t in range(T):
        nthreads = {}

        for k,v in threads.items():
            bots,res = list(int(a) for a in k[:4]), list(int(a) for a in k[4:])
            res1 = res
            res = (res[0]+bots[0], res[1]+bots[1], res[2]+bots[2])
            v = v + bots[3]

            # Key to keeping number of states manageable:
            # If we have enough ore, only explore options that do somehting
            # DO NOT add states that do nothing, when we can do something -- it never helps.
            if res1[0] < MO and res1[1] < obsClay and res1[2] < geodeObs:
                kk = HASH((bots[0], bots[1], bots[2], bots[3], res[0], res[1], res[2]))
                if kk in nthreads: nthreads[kk] = max(v, nthreads[kk])
                else: nthreads[kk] = v

            # Explore all options
            if res1[0] >= oreOre:
                kk = HASH((bots[0]+1, bots[1], bots[2], bots[3], res[0]-oreOre, res[1], res[2]))
                if kk in nthreads: nthreads[kk] = max(v, nthreads[kk])
                else: nthreads[kk] = v
            if res1[0] >= clayOre:
                kk = HASH((bots[0], bots[1]+1, bots[2], bots[3], res[0]-clayOre, res[1], res[2]))
                if kk in nthreads: nthreads[kk] = max(v, nthreads[kk])
                else: nthreads[kk] = v
            if res1[0] >= obsOre and res1[1] >= obsClay:
                kk = HASH((bots[0], bots[1], bots[2]+1, bots[3], res[0]-obsOre, res[1]-obsClay, res[2]))
                if kk in nthreads: nthreads[kk] = max(v, nthreads[kk])
                else: nthreads[kk] = v
            if res1[0] >= geodeOre and res1[2] >= geodeObs:
                kk = HASH((bots[0], bots[1], bots[2], bots[3]+1, res[0]-geodeOre, res[1], res[2]-geodeObs))
                if kk in nthreads: nthreads[kk] = max(v, nthreads[kk])
                else: nthreads[kk] = v
        # print('t', t, 'nthreads', len(nthreads))

        # prune on max-min resource
        bestHeads = {}
        nnthreads = {}
        for k,v in nthreads.items():
            bots,res = tuple(int(a) for a in k[:4]), tuple(int(a) for a in k[4:])
            mr = min(res[:3])
            if bots not in bestHeads or (mr > bestHeads[bots][0] and v > bestHeads[bots][1]): bestHeads[bots] = mr,v
        for k,v in nthreads.items():
            bots,res = tuple(int(a) for a in k[:4]), tuple(int(a) for a in k[4:])
            maxr = max(res[:3])
            if maxr >= bestHeads[bots][0] and v >= bestHeads[bots][1]: nnthreads[HASH(list(bots)+list(res))] = v
        nthreads = nnthreads

        threads = nthreads

    o = max((v for v in threads.values()))
    print(b,'->',o)
    return o

# PART 1
if 1:
    acc = 0
    for i,BB in enumerate(B):
        o = solveOne(*BB)
        acc += (i+1) * o
        print(' - add', (i+1)*o)
    print(' - final', acc)

# PART 2
print(' - final part 2:', solveOne(*B[0],T=32)*solveOne(*B[1],T=32)*solveOne(*B[2],T=32))
