# https://www.acmicpc.net/problem/1929

import math

M, N = map(int, input().split())
prime = [i for i in range(N+1)]
for i in range(2, int(math.sqrt(N))+1):
    if prime[i] != 1:
        j = 2
        while i * j < len(prime):
            prime[i * j] = 1
            j += 1
for p in range(M, N+1):
    if prime[p] != 1: print(prime[p])