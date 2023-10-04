# https://www.acmicpc.net/problem/1743

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
food = [[0] * M for _ in range(N)]
for i in range(K):
    r, c = map(int, input().split())
    food[r-1][c-1] = 1
visited = [[False] * M for _ in range(N)]
food_size = []
q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if not visited[i][j] and food[i][j]:
            q.append([i, j])
            visited[i][j] = True
            cnt = 1
            while q:
                qp = q.popleft()
                for k in range(4):
                    di, dj = qp[0] + dy[k], qp[1] + dx[k]
                    if N > di >= 0 and M > dj >= 0 and food[di][dj] and not visited[di][dj]:
                        visited[di][dj] = True
                        q.append([di, dj])
                        cnt += 1
            food_size.append(cnt)
print(max(food_size))