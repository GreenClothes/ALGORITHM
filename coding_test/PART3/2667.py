# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
MAP = [list(input().strip()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[False] * N for i in range(N)]
q = deque()
cnt_total = []

for i in range(N):
    for j in range(N):
        if MAP[i][j] != '0' and not visited[i][j]:
            q.append([i, j])
            visited[i][j] = True
            cnt = 0
            while q:
                cnt += 1
                visit = q.popleft()

                for k in range(4):
                    di, dj = visit[0]+dy[k], visit[1]+dx[k]
                    if N>di>=0 and N>dj>=0 and not visited[di][dj] and MAP[di][dj]=='1':
                        q.append([di, dj])
                        visited[di][dj] = True
            cnt_total.append(cnt)

cnt_total = sorted(cnt_total)
print(len(cnt_total))
for i in range(len(cnt_total)):
    print(cnt_total[i])
