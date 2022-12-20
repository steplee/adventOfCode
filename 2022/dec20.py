import sys
import re
lines = [l.strip() for l in sys.stdin.readlines()]

f = [int(f) for f in lines]
g = list(f)
N = len(g)

KEY = 1
KEY = 811589153
ROUNDS = 1
ROUNDS = 10

# from collections import namedtuple
# Node = namedtuple('Node', 'v prv nxt'.split(' '))
class Node:
    def __init__(self, v, p, n):
        self.v, self.prv, self.nxt = v,p,n
    def __repr__(self):
        return ('<{} {} {}>'.format(self.v, self.prv, self.nxt))

nodes = [Node(KEY*v, (i-1)%N, (i+1)%N) for (i,v) in enumerate(f)]
# print('original')
# print(nodes)

from copy import deepcopy

for round in range(ROUNDS):

    for i_, ff in enumerate(f):
        # print(i_,'/',len(f))
        it = i_

        currNode = nodes[it]

        ff = ff * KEY
        ff = (ff % (N-1)) if ff > 0 else (ff % -(N-1))

        if ff != 0:

            # The key was to not move multiple spots in one iteration:
            # instead make multiple iteratiosn of removing and inseritng.
            for iter in range(abs(ff)):
                ff = 1 if ff >= 1 else -1

                # Delete: Re-route old neighbors
                oldBack = currNode.prv
                oldNext = currNode.nxt
                nodes[currNode.prv].nxt = oldNext # next(my_prev) = my_next
                nodes[currNode.nxt].prv = oldBack # prev(my_next) = my_prev

                onePastIdx = it
                onePrevIdx = it

                # Insert
                if ff>0:
                    for ii in range(abs(ff)):
                        onePrevIdx = nodes[onePrevIdx].nxt if ff>0 else nodes[onePrevIdx].prv

                    onePrev = nodes[onePrevIdx]

                    onePastIdx = nodes[onePrevIdx].nxt
                    onePast = nodes[onePastIdx]

                    onePrev.nxt = it
                    onePast.prv = it
                    currNode.prv = onePrevIdx
                    currNode.nxt = onePastIdx

                else:
                    for ii in range(abs(ff)):
                        onePrevIdx = nodes[onePrevIdx].nxt if ff>0 else nodes[onePrevIdx].prv

                    onePrev = nodes[onePrevIdx]

                    onePastIdx = nodes[onePrevIdx].prv
                    onePast = nodes[onePastIdx]

                    onePrev.prv = it
                    onePast.nxt = it
                    currNode.nxt = onePrevIdx
                    currNode.prv = onePastIdx

    zidx = 0
    for idx,(node) in enumerate(nodes):
        if node.v == 0:
            zidx = idx
            break

    '''
    idx = zidx
    print(' - FROM ZERO')
    for i in range(len(f)):
        print(nodes[idx])
        idx = nodes[idx].nxt
    '''

    acc = 0
    idx = zidx
    for i in range(3001):
        if i > 0 and i % 1000 == 0:
            # print('add',nodes[idx].v, 'from', idx)
            acc += nodes[idx].v
        idx = nodes[idx].nxt
    print('answer', acc)
