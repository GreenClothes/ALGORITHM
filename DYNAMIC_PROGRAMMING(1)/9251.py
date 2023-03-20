# https://www.acmicpc.net/problem/9251

import sys

S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
dp = [0] * len(S2)

for i in range(len(S1)):
    cache = 0
    for j in range(len(S2)):
        if cache < dp[j]:
            cache = dp[j]
        elif S1[i] == S2[j]:
            dp[j] = cache + 1
print(max(dp))