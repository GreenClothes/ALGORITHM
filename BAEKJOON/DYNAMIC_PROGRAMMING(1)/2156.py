# https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline

n = int(input().strip())
wine = [int(input().strip()) for _ in range(n)]
dp = [0] * n

if n <= 2:
    print(sum(wine))
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2])
    for i in range(3, n):
        dp[i] = max(wine[i] + wine[i-1] + dp[i-3], wine[i] + wine[i-1] + dp[i-4], wine[i] + wine[i-2] + dp[i-4],
                    wine[i] + dp[i-2])
    if dp[-1] > dp[-2]: print(dp[-1])
    else: print(dp[-2])
