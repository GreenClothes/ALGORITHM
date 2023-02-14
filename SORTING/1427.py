# https://www.acmicpc.net/problem/1427

import sys

N = sorted([int(i) for i in sys.stdin.readline().strip()], reverse=True)
for n in N:
    print(n, end='')