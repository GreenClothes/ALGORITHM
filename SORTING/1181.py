# https://www.acmicpc.net/problem/1181

import sys

N = sorted({sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline().strip()))})
print(*sorted(N, key=lambda x: len(x)), sep='\n')