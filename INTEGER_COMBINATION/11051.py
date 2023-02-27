# https://www.acmicpc.net/problem/11051

import sys
N, K = map(int, sys.stdin.readline().strip().split())

if K > N//2: K = N - K
C = [0] * (K+1)
C[0] = 1

for i in range(1, N+1):
    j = min(i, K)
    while j > 0:
        C[j] = C[j] + C[j-1]
        j -= 1

print(C[K]%10007)