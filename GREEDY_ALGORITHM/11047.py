# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
C = [int(input().strip()) for _ in range(N)]
C_num = 0

while N:
    N -= 1
    if K >= C[N]:
        C_num += (K // C[N])
        K %= C[N]
    if K == 0:
        print(C_num)
        break