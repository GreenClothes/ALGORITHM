# https://www.acmicpc.net/problem/11651

import sys

N = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))]
N.sort(key=lambda x: x[0])
N.sort(key=lambda x: x[1])
for i in range(len(N)): print(*N[i])