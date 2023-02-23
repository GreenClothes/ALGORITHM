# https://www.acmicpc.net/problem/10815

import sys

sys.stdin.readline().strip()
N = set(list(map(int, sys.stdin.readline().strip().split())))
sys.stdin.readline().strip()
M = list(map(int, sys.stdin.readline().strip().split()))
NM_inter = N & set(M)

for m in M:
    if m in NM_inter:
        print('1', end=' ')
    else:
        print('0', end=' ')