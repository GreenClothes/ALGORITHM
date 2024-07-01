# https://www.acmicpc.net/problem/15651

import sys

def permutation(N, M):
    if len(p) == M:
        print(*p)
        return

    for i in range(1, N+1):
        p.append(i)
        permutation(N, M)
        p.pop()

N, M = map(int, sys.stdin.readline().strip().split())
p = []
permutation(N, M)