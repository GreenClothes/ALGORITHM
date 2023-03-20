# https://www.acmicpc.net/problem/11659

import sys

N, M = map(int, sys.stdin.readline().strip().split())
num = list(map(int, sys.stdin.readline().strip().split()))
for i in range(1, len(num)):
    num[i] = num[i] + num[i-1]
num.append(0)

for k in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(num[j-1] - num[i-2])