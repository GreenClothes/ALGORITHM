# https://www.acmicpc.net/problem/14425

import sys

n, m = map(int, sys.stdin.readline().strip().split())
N = set(sys.stdin.readline().strip() for _ in range(n))

MinN = 0
for i in range(m):
    if sys.stdin.readline().strip() in N:
        MinN += 1
print(MinN)