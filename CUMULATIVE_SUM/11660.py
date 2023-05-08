# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
T = [list(map(int, input().strip().split())) for _ in range(N)]
for i in range(N):
    for j in range(1, N):
        T[i][j] += T[i][j-1]

for i in range(M):
    y1, x1, y2, x2 = map(int, input().strip().split())
    c_sum = 0
    for j in range(y1-1, y2):
        if x1 == 1:
            c_sum += T[j][x2-1]
        else:
            c_sum += (T[j][x2-1] - T[j][x1-2])
    print(c_sum)