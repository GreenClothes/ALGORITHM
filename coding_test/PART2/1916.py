# https://www.acmicpc.net/problem/1916

import heapq
from sys import maxsize

N = int(input())
M = int(input())
BUS = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    BUS[a].append((b, c))
start, end = map(int, input().split())
visited = {i:maxsize for i in range(N+1)}

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    visited[s] = 0

    while q:
        cost, bus = heapq.heappop(q)

        if visited[bus] < cost:
            continue

        for next_bus, next_cost in BUS[bus]:
            expect_cost = cost + next_cost

            if visited[next_bus] > expect_cost:
                heapq.heappush(q, (expect_cost, next_bus))
                visited[next_bus] = expect_cost

dijkstra(start)
print(visited[end])