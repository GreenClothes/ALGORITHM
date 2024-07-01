# https://www.acmicpc.net/problem/2231

import sys

N = N_prime = int(sys.stdin.readline().strip())
make = []
while N_prime != 0:
    N_prime -= 1
    n = [int(s) for s in str(N_prime)]
    if N_prime + sum(n) == N : make.append(N_prime)
print(min(make) if make else '0')