# https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline

n = int(input().strip())
N = list(map(int, input().strip().split()))
dp = [0] * n
dp[0] = N[0]

for i in range(1, n):
    dp[i] = max(N[i], N[i] + dp[i-1])

print(max(dp))