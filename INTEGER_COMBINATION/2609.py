# https://www.acmicpc.net/problem/2609

import sys

N, M = map(int, sys.stdin.readline().strip().split())
if N < M:
    temp = N
    N = M
    M = temp
div, mul = 1, N*M
for i in range(N, 0, -1):
    if N%i == 0 and M%i == 0:
        div = i
        break
for i in range(1, N):
    if N*i%M == 0:
        mul = N*i
        break
print(div, mul, sep='\n')