# https://www.acmicpc.net/problem/2565

import sys

N = int(sys.stdin.readline().strip())
line = sorted([list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)])
dp = [1] * N

for i in range(N):
    for j in range(i):
        if line[i][1] > line[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))