import sys

flow = {}
graph = {}
for line in sys.stdin.readlines():
    line = line.strip()
    parts = line.split(' ')
    it = parts[1]
    rate = int(parts[4].split('=')[1][:-1])
    tos = [p.replace(',','') for p in parts[9:]]

    graph[it] = tos
    flow[it] = rate

# <cur accScore open>

# Version 1: had a lot of extras because I kept multiple states with better/worse scores,
'''
threads = [('AA',0,set())]

seen = set()

for time in range(10):
    nthreads = []

    for (cur,score,opened) in threads:

        rate = sum(flow[k] for k in opened)
        print(rate,opened)
        score += rate

        # Each step we can open current, or move to next
        if flow[cur] > 0 and cur not in opened:
            opened2 = set(opened)
            opened2.add(cur)
            st = '{}_{}_{}'.format(cur,score,'_'.join(sorted(list(opened2))))
            if st not in seen:
                nthreads.append((cur,score,opened2))
                # seen.add(st)

        for nxt in graph[cur]:
            st = '{}_{}_{}'.format(nxt,score,'_'.join(sorted(list(opened))))
            if st not in seen:
                nthreads.append((nxt,score,opened))
                seen.add(st)

    print(' - time {}, nthreads {}'.format(time,len(nthreads)))
    threads = nthreads
'''

# Version 2: Keep sorted list (not set) and do not keep *only* single best
# thread with the same (cur, opened) pair, but the highest score

threads = [('AA',0,[])]
seen = set()

for time in range(30):
    nthreads = []
    grps = {}
    for (cur,score,opened) in threads:

        rate = sum(flow[k] for k in opened)
        # print(rate,opened)
        score += rate

        # Each step we can open current, or move to next
        if flow[cur] > 0 and cur not in opened:
            opened2 = list(opened)
            opened2.append(cur)
            opened2 = sorted(opened2)
            st = '{}_{}'.format(cur,'_'.join(opened2))
            if st not in grps: grps[st] = score
            elif score > grps[st]: grps[st] = score

        for nxt in graph[cur]:
            st = '{}_{}'.format(nxt,'_'.join(opened))
            if st not in grps: grps[st] = score
            elif score > grps[st]: grps[st] = score

    for k,score in grps.items():
        it, *opened = k.split('_')
        opened = [o for o in opened if len(o) > 0]
        nthreads.append( (it, score, opened) )
    threads = nthreads
    print(' - time {}, nthreads {}'.format(time,len(nthreads)))

print(max([s for (c,s,o) in threads]))






# Part 2
#
# It is not pretty, but it does work...



threads = [('AA','AA',0,[])]
seen = set()

for time in range(26):
    nthreads = []
    grps = {}
    for (cur1,cur2,score,opened) in threads:

        rate = sum(flow[k] for k in opened)
        # print(rate,opened)
        score += rate

        cur1, cur2 = min(cur1, cur2), max(cur1, cur2)

        opt1 = []
        opt2 = []

        if flow[cur1] > 0 and cur1 not in opened:
            opened2 = sorted(opened + [cur1])
            opt1.append( (cur1, cur2, opened2) )

        for nxt in graph[cur1]:
            # ncur1, ncur2 = min(nxt, cur2), max(nxt, cur2)
            ncur1, ncur2 = nxt, cur2
            opt1.append( (ncur1, ncur2, opened) )

        if flow[cur2] > 0 and cur2 not in opened:
            opened2 = sorted(opened + [cur2])
            opt2.append( (cur1, cur2, opened2) )

        for nxt in graph[cur2]:
            # ncur1, ncur2 = min(cur1, nxt), max(cur1, nxt)
            ncur1, ncur2 = cur1, nxt
            opt2.append( (ncur1, ncur2, opened) )

        for it11, it12, o1 in opt1:
            for it21, it22, o2 in opt2:

                # it11,it21 = min(it11, it21), max(it11, it21)
                # it12,it22 = min(it12, it22), max(it12, it22)
                # it11,it12 = min(it11, it12), max(it11, it12)
                # it21,it22 = min(it21, it22), max(it21, it22)

                ooo = (sorted(list(set((o1+o2)))))
                # oo = '_'.join(sorted(list(set((o1+o2)))))
                oo = sum(flow[k] for k in list(set(o1+o2)))

                st = '{}_{}_{}'.format(it21,it22,oo)
                if st not in grps: grps[st] = score,ooo
                elif score > grps[st][0]: grps[st] = score,ooo

                st = '{}_{}_{}'.format(it11,it22,oo)
                if st not in grps: grps[st] = score,ooo
                elif score > grps[st][0]: grps[st] = score,ooo

                st = '{}_{}_{}'.format(it21,it12,oo)
                if st not in grps: grps[st] = score,ooo
                elif score > grps[st][0]: grps[st] = score,ooo

                st = '{}_{}_{}'.format(it11,it12,oo)
                if st not in grps: grps[st] = score,ooo
                elif score > grps[st][0]: grps[st] = score,ooo

                # print(st)


            # if st not in grps: grps[st] = score
            # elif score > grps[st]: grps[st] = score

    for k,(score,opened) in grps.items():
        it1, it2, r = k.split('_')
        # opened = [o for o in opened if len(o) > 0]
        nthreads.append( (it1, it2, score, opened) )
        # nthreads.append( (min(it1, it2, score, opened) )
        # nthreads.append( (it2, it1, score, opened) )
    threads = nthreads
    print(' - time {}, nthreads {}'.format(time,len(nthreads)))

print(max([s for (c,cc,s,o) in threads]))


