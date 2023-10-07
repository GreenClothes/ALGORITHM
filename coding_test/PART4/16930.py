# https://www.acmicpc.net/problem/16930

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
gym = [list(input()) for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[10000] * M for _ in range(N)]
visited[x1-1][y1-1] = 0
q = deque()
q.append((x1-1, y1-1))

while q:
    x, y = q.popleft()
    if x == x2-1 and y == y2-1:
        break

    for i in range(4):
        j = 0
        di, dj = x + dx[i], y + dy[i]
        while N>di>=0 and M>dj>=0  and j < K and gym[di][dj] == '.' and visited[di][dj] > visited[x][y]:
            if visited[di][dj] == 10000:
                visited[di][dj] = visited[x][y] + 1
                q.append((di, dj))
            di, dj = di + dx[i], dj + dy[i]
            j += 1
ans = visited[x2-1][y2-1]
if ans == 10000:
    print(-1)
else:
    print(ans)