# https://www.acmicpc.net/problem/1197

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
tree = [[] for _ in range(V+1)]
for e in range(E):
    a, b, c = map(int, input().split())
    tree[a].append((c, b))
    tree[b].append((c, a))
visited = {i:False for i in range(1, V+1)}
total_cost = 0

q = []
for v in range(1, V+1):
    heapq.heappush(q, (0, 1))
    while q:
        cost, visit = heapq.heappop(q)
        if not visited[visit]:
            visited[visit] = True
            total_cost += cost
            for next_cost, next_visit in tree[visit]:
                heapq.heappush(q, (next_cost, next_visit))

print(total_cost)