# https://www.acmicpc.net/problem/2579

import sys

n = int(sys.stdin.readline().strip())
stair = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [0] * n

if n <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[-1])