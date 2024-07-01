# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = {i:[0]*(N+1) for i in range(1, N+1)}
visited = {i:False for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    print(v, end=' ')
    for i in range(1, N+1):
        if not visited[i] and graph[v][i]:
            visited[i] = True
            dfs(i)
visited[V] = True
dfs(V)

print()
q = deque()
q.append(V)
visited[V] = False
while q:
    qp = q.popleft()
    print(qp, end=' ')
    for i in range(1, N+1):
        if visited[i] and graph[qp][i]:
            visited[i] = False
            q.append(i)