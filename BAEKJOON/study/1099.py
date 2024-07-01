# https://www.acmicpc.net/problem/1099

import sys
input = sys.stdin.readline

S = ' ' + input().strip()
N = int(input())
W = [input().strip() for _ in range(N)]

def cost(w1, w2, length):
    cnt = 0
    for i in range(length):
        if w1[i] != w2[i]:
            cnt += 1
    return cnt

dp = [[1000]*(len(S)) for _ in range(len(S))]
dp[0][0] = 0

for i in range(1, len(S)+1):
    if dp[i-1][0] == 1000:
        continue
    for w in W:
        l_w = len(w)
        if sorted(S[i:i+l_w]) == sorted(w):
            dp[i][i+l_w-1] = min(dp[i][i+l_w-1], dp[i-1][0]+cost(S[i:i+l_w], w, l_w))
            dp[i+l_w-1][0] = min(dp[i+l_w-1][0], dp[i][i+l_w-1])

print(dp[-1][0] if dp[-1][0] != 1000 else -1)