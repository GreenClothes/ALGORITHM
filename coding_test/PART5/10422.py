# https://www.acmicpc.net/problem/10422

import sys
input = sys.stdin.readline

T = int(input())
L = [int(input()) for t in range(T)]
dp = [0 for i in range(max(L)//2+1)]
dp[0] = 1
dp[1] = 1
for i in range(2, len(dp)):
    for j in range(i):
        dp[i] += (dp[i-j-1]*dp[j])
        dp[i] %= 1000000007

for t in range(T):
    if L[t] % 2:
        print(0)
    else:
        print(dp[L[t]//2])