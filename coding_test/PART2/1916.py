# https://www.acmicpc.net/problem/1916

import heapq

N = int(input())
M = int(input())
BUS = {i:dict() for i in range(N+1)}
for _ in range(M):
    a, b, c = map(int, input().split())
    BUS[a][b] = c
start, end = map(int, input().split())
visited = {i:100000 for i in range(N+1)}

def dijkstra(s):
    q = []
    heapq.heappush(q, (s, 0))
    visited[s] = 0

    while q:
        bus, cost = heapq.heappop(q)

        if visited[bus] < cost:
            continue

        for next_bus, next_cost in BUS[bus].items():
            expect_cost = cost + next_cost

            if visited[next_bus] > expect_cost:
                heapq.heappush(q, (next_bus, expect_cost))
                visited[next_bus] = expect_cost

dijkstra(start)
print(visited[end])