# https://www.acmicpc.net/problem/10451

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs():
    cycle = 0
    q = deque()
    for i in range(1, N+1):
        if not visited[i]:
            q.append(i)
            while q:
                qp = q.popleft()
                visited[qp] = True
                if not visited[graph[qp]]:
                    q.append(graph[qp])
            cycle += 1
    print(cycle)

for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    graph = {i:0 for i in range(1, N+1)}
    visited = {i:False for i in range(1, N+1)}
    for p in range(len(P)):
        graph[p+1] = P[p]
    bfs()
