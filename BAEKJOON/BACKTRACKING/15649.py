# https://www.acmicpc.net/problem/15649

import sys

N, M = map(int, sys.stdin.readline().strip().split())
p = []

def permutation(N, M):
    global p
    if len(p) == M:
        print(*p)
        return

    for i in range(1, N+1):
        if i not in p:
            p.append(i)
            permutation(N, M)
            p.pop()
permutation(N, M)
