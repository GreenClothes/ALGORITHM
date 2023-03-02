# https://www.acmicpc.net/problem/15652

import sys

def permutation(N, M, start):
    if len(p) == M:
        print(*p)
        return

    for i in range(start, N+1):
        p.append(i)
        permutation(N, M, p[-1])
        p.pop()

N, M = map(int, sys.stdin.readline().strip().split())
p = []
permutation(N, M, 1)