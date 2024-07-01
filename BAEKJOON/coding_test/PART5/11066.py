# https://www.acmicpc.net/problem/11066

import sys
from sys import maxsize
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    file = list(map(int, input().split()))
    dp = [[0] * K for _ in range(K)]
    file_sum = {-1:0}
    for i in range(K):
        file_sum[i] = file_sum[i-1] + file[i]
    for term in range(1, K):
        for start in range(K-1):
            end = start + term
            if end >= len(file):
                break
            result = maxsize
            for cut in range(start, end):
                result = min(result, dp[start][cut] + dp[cut+1][end] + file_sum[end] - file_sum[start-1])
            dp[start][end] = result
    print(dp[0][-1])