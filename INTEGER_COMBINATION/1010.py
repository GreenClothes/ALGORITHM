# https://www.acmicpc.net/problem/1010

import sys

for i in range(int(sys.stdin.readline().strip())):
    N, M = map(int, sys.stdin.readline().strip().split())

    if N > M // 2: N = M - N

    C = [0] * (N+1)
    C[0] = 1
    for j in range(M+1):
        k = min(j, N)
        while k > 0:
            C[k] = C[k] + C[k-1]
            k -= 1
    print(C[N])