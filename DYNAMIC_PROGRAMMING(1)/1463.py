# https://www.acmicpc.net/problem/1463

import sys

N = int(sys.stdin.readline().strip())
n = [1e9] * (N+1)
n[N] = 0

for i in range(N, 0, -1):
    if i % 3 == 0:
        n[i//3] = min(n[i//3], n[i]+1)
    if i % 2 == 0:
        n[i//2] = min(n[i//2], n[i]+1)
    n[i-1] = min(n[i-1], n[i]+1)

print(n[1])