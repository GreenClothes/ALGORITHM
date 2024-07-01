# https://www.acmicpc.net/problem/1303

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
war = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
soldier = deque()
team = {0:'W', 1:'B'}
power = [0, 0]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def count(x, y, s):
    cnt = 0
    soldier.append([x, y])
    while soldier:
        s_xy = soldier.popleft()
        cnt += 1
        for d in range(4):
            di, dj = s_xy[1] + dy[d], s_xy[0] + dx[d]
            if M > di >= 0 and N > dj >= 0 and not visited[di][dj] and war[di][dj] == team[s]:
                visited[di][dj] = True
                soldier.append([dj, di])
    power[s] += cnt**2


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            if war[i][j] == 'W':
                count(j, i, 0)
            else:
                count(j, i, 1)

print(power[0], power[1])

