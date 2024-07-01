# https://www.acmicpc.net/problem/2206

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
NMmap = [list(input().rstrip()) for _ in range(N)]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]
q = deque()
q.append([0, 0, 0, 1])
visited[0][0][0] = True

def bfs():
    while q:
        y, x, b, c = q.popleft()
        if y == N-1 and x == M-1:
            return c
        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            dy += y
            dx += x
            if 0 <= dy < N and 0 <= dx < M:
                if not visited[dy][dx][b]:
                    if int(NMmap[dy][dx]) and not b and not visited[dy][dx][1]:
                        visited[dy][dx][1] = True
                        q.append([dy, dx, 1, c+1])
                    elif not int(NMmap[dy][dx]) and not visited[dy][dx][b]:
                        visited[dy][dx][b] = True
                        q.append([dy, dx, b, c+1])
    return -1
print(bfs())
