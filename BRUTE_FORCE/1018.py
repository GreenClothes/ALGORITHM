# https://www.acmicpc.net/problem/1018

import sys

N, M = map(int, sys.stdin.readline().strip().split())
board = [[s for s in sys.stdin.readline().strip()] for _ in range(N)]
repaint = []

for n in range(8, N+1):
    for m in range(8, M+1):
        repaint_1_cnt = 0
        repaint_2_cnt = 0
        for i in range(n-8, n):
            for j in range(m-8, m):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W': repaint_1_cnt += 1
                    if board[i][j] != 'B': repaint_2_cnt += 1
                else:
                    if board[i][j] != 'W': repaint_2_cnt += 1
                    if board[i][j] != 'B': repaint_1_cnt += 1

        repaint.append(repaint_1_cnt)
        repaint.append(repaint_2_cnt)

print(min(repaint))