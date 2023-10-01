# https://www.acmicpc.net/problem/2294

import sys
from sys import maxsize
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
dp = {i:maxsize for i in range(k+1)}
dp[0] = 0

for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c]+1)

print(dp[k] if dp[k] < maxsize else -1)