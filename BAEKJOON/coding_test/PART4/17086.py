# https://www.acmicpc.net/problem/17086

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
distance = [[100] * M for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

max_distance = 0
q = deque()

for i in range(N):
    for j in range(M):
        if space[i][j]:
            q.append((i, j))
            distance[i][j] = 0
            while q:
                y, x = q.popleft()
                for k in range(8):
                    di, dj = y+dy[k], x+dx[k]
                    if N>di>=0 and M>dj>=0 and distance[di][dj] > distance[y][x] + 1 and not space[di][dj]:
                        distance[di][dj] = distance[y][x] + 1
                        q.append((di, dj))
for i in range(N):
    max_d = max(distance[i])
    if max_d > max_distance:
        max_distance = max_d
print(max_distance)