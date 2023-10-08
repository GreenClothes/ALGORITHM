# https://www.acmicpc.net/problem/1495

import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
volume = list(map(int, input().split()))
V = [[0] * (M+1) for _ in range(N+1)]
V[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if V[i-1][j]:
            P_minus = j - volume[i-1]
            P_plus = j + volume[i-1]
            if P_minus >= 0:
                V[i][P_minus] = 1
            if P_plus <= M:
                V[i][P_plus] = 1
for i in range(M, -1, -1):
    if V[N][i]:
        print(i)
        exit()
print(-1)