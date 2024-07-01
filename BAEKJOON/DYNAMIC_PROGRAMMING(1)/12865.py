# https://www.acmicpc.net/problem/12865

import sys

N, K = map(int, sys.stdin.readline().strip().split())
WV = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
value = [0] * (K+1)

for i in range(N):
    for j in range(K, 0, -1):
        if WV[i][0] <= j:
            value[j] = max(value[j], value[j - WV[i][0]] + WV[i][1])
print(max(value))