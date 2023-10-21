# https://www.acmicpc.net/problem/1726

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(M)]
sm, sn, sd = map(int, input().split())
em, en, ed = map(int, input().split())
visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]
dm = [0, 0, 1, -1]
dn = [1, -1, 0, 0]
change = [(2, 3), (2, 3), (0, 1), (0, 1)]

def bfs():
    q = deque()
    q.append([sm-1, sn-1, sd-1, 0])
    visited[sm-1][sn-1][sd-1] = True

    while q:
        y, x, d, c = q.popleft()
        if (y, x, d) == (em-1, en-1, ed-1):
            return c
        for go in range(1, 4):
            dy, dx = y + go*dm[d], x + go*dn[d]
            if 0 <= dy < M and 0 <= dx < N:
                if factory[dy][dx]:
                    break
                if not visited[dy][dx][d]:
                    visited[dy][dx][d] = True
                    q.append([dy, dx, d, c+1])
            else:
                break
        for dd in change[d]:
            if not visited[y][x][dd]:
                visited[y][x][dd] = True
                q.append([y, x, dd, c+1])
print(bfs())