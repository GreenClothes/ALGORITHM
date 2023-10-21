# https://www.acmicpc.net/problem/2146

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
q = deque()
next_q = deque()
edge = False
cnt = 1

for y in range(N):
    for x in range(N):
        if MAP[y][x] and not visited[y][x]:
            q.append((y, x))
            visited[y][x] = True
            while q:
                i, j = q.popleft()
                MAP[i][j] = cnt
                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    di += i
                    dj += j
                    if 0 <= di < N and 0 <= dj < N:
                        if not visited[di][dj]:
                            if MAP[di][dj]:
                                visited[di][dj] = True
                                q.append([di, dj])
                            else:
                                edge = True
                if edge:
                    next_q.append([i, j, cnt, 0])
                    edge = False
            cnt += 1
dist = [[0] * N for _ in range(N)]
min_dist = sys.maxsize
while next_q:
    i, j, c, d = next_q.popleft()
    MAP[i][j] = c
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        di += i
        dj += j
        if 0 <= di < N and 0 <= dj < N:
            if MAP[di][dj] != 0 and MAP[di][dj] != c:
                min_dist = min(min_dist, d+dist[di][dj])
            if not MAP[di][dj] and not dist[di][dj]:
                next_q.append([di, dj, c, d+1])
                dist[di][dj] = d+1
            elif not MAP[di][dj] and d+1 < dist[di][dj]:
                dist[di][dj] = d+1
                next_q.append([di, dj, c, d+1])
if min_dist == sys.maxsize:
    print(0)
else:
    print(min_dist)

