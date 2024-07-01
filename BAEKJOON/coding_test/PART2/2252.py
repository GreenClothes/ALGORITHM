# https://www.acmicpc.net/problem/2252

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
q = [[] for _ in range(N+1)]
degree = {i:0 for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    q[a].append(b)
    degree[b] += 1

dq = deque([])
result = []

for n in range(1, N+1):
    if degree[n] == 0:
        dq.append(n)
while dq:
    d = dq.popleft()
    for b in q[d]:
        degree[b] -= 1
        if degree[b] == 0:
            dq.append(b)
    result.append(d)

print(*result)