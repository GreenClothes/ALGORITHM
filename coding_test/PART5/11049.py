# https://www.acmicpc.net/problem/11049
# https://ddiyeon.tistory.com/72

import sys
input = sys.stdin.readline

N = int(input())
rc = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for num in range(N-1):
    for start in range(N-num-1):
        i = num + start + 1
        dp[start][i] = 2**31

        for t in range(start, i):
            dp[start][i] = min(dp[start][i], dp[start][t] + dp[t+1][i] + rc[start][0]*rc[t][1]*rc[i][1])
print(dp[0][N-1])
