# https://www.acmicpc.net/problem/2606

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
P = int(input())
pair = {i:[] for i in range(1, N+1)}
for _ in range(P):
    a, b = map(int, input().split())
    pair[a].append(b)
    pair[b].append(a)
visited = [False] * (N+1)
q = deque()
q.append(1)
visited[1] = True

while q:
    qp = q.popleft()
    for p in pair[qp]:
        if not visited[p]:
            q.append(p)
            visited[p] = True
print(visited.count(True)-1)
