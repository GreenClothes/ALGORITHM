# https://www.acmicpc.net/problem/16197

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
coins = []
for n in range(N):
    for m in range(M):
        if board[n][m] == 'o':
            coins.append([n, m])
coins.append(0)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
q.append(coins)

while q:
    qp = q.popleft()
    if qp[2] >= 10:
        print(-1)
        exit()
    for i in range(4):
        dc1_y, dc1_x, dc2_y, dc2_x = qp[0][0] + dy[i], qp[0][1] + dx[i], qp[1][0] + dy[i], qp[1][1] + dx[i]
        if N>dc1_y>=0 and M>dc1_x>=0 and N>dc2_y>=0 and M>dc2_x>=0:
            if board[dc1_y][dc1_x] == '#' and board[dc2_y][dc2_x] == '#':
                pass
            else:
                if board[dc1_y][dc1_x] == '#':
                    dc1_y, dc1_x = qp[0][0], qp[0][1]
                if board[dc2_y][dc2_x] == '#':
                    dc2_y, dc2_x = qp[1][0], qp[1][1]
                q.append([[dc1_y, dc1_x], [dc2_y, dc2_x], qp[2]+1])
        elif (N>dc1_y>=0 and M>dc1_x>=0) != (N>dc2_y>=0 and M>dc2_x>=0):
            print(qp[2]+1)
            exit()
print(-1)

