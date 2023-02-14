# https://www.acmicpc.net/problem/11650

import sys

N = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip()))])
for i in range(len(N)):
    print(*N[i])