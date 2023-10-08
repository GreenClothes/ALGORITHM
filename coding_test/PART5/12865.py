# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
value = [0] * (K+1)

for i in range(N):
    for j in range(K, 0, -1):
        if WV[i][0] <= j:
            value[j] = max(value[j], value[j - WV[i][0]] + WV[i][1])

print(max(value))