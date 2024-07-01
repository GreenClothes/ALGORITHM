# https://www.acmicpc.net/problem/10942

import sys
input = sys.stdin.readline

N = int(input())
N_num = list(map(int, input().split()))
M = int(input())
M_q = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * N for _ in range(N)]

for term in range(N):
    for start in range(N):
        if term == 0:
            dp[start][start] = 1
            continue
        end = start + term
        if end >= N:
            break
        dp[end][start] = 1
        if dp[start+1][end-1]:
            if N_num[start] == N_num[end]:
                dp[start][end] = 1
            else:
                dp[start][end] = 0
        else:
            dp[start][end] = 0
for q in M_q:
    print(dp[q[0]-1][q[1]-1])

