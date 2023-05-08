# https://www.acmicpc.net/problem/25682

import sys
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
C = [input().strip() for _ in range(N)]

wC, bC = [[0]*(M+1) for _ in range(N+1)], [[0]*(M+1) for _ in range(N+1)]
repaint = []

for n in range(1, N+1):
    for m in range(1, M+1):
        if (n+m)%2 == 0:
            if C[n-1][m-1] != 'W': wC[n][m] = wC[n-1][m] + wC[n][m-1] - wC[n-1][m-1] + 1
            else: wC[n][m] = wC[n-1][m] + wC[n][m-1] - wC[n-1][m-1]
            if C[n-1][m-1] != 'B': bC[n][m] = bC[n-1][m] + bC[n][m-1] - bC[n-1][m-1] + 1
            else: bC[n][m] = bC[n - 1][m] + bC[n][m - 1] - bC[n - 1][m - 1]
        else:
            if C[n-1][m-1] != 'W': bC[n][m] = bC[n-1][m] + bC[n][m-1] - bC[n-1][m-1] + 1
            else: bC[n][m] = bC[n - 1][m] + bC[n][m - 1] - bC[n - 1][m - 1]
            if C[n-1][m-1] != 'B': wC[n][m] = wC[n-1][m] + wC[n][m-1] - wC[n-1][m-1] + 1
            else: wC[n][m] = wC[n - 1][m] + wC[n][m - 1] - wC[n - 1][m - 1]
for i in range(N-K+1):
    for j in range(M-K+1):
        repaint.append(wC[i+K][j+K] - wC[i][j+K] - wC[i+K][j] + wC[i][j])
        repaint.append(bC[i+K][j+K] - bC[i][j+K] - bC[i+K][j] + bC[i][j])
print(min(repaint))

