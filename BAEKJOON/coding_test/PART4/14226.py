# https://www.acmicpc.net/problem/14226

from collections import deque
S = int(input())
imo = dict()
imo[(1, 0)] = 0
q = deque()
q.append((1, 0))

while q:
    t, c = q.popleft()
    if t == S:
        print(imo[(t, c)])
        break

    if (t, t) not in imo.keys():
        imo[(t, t)] = imo[(t, c)] + 1
        q.append((t, t))
    if (t+c, c) not in imo.keys():
        imo[(t+c, c)] = imo[(t, c)] + 1
        q.append((t+c, c))
    if (t-1, c) not in imo.keys():
        imo[(t-1, c)] = imo[(t, c)] + 1
        q.append((t-1, c))