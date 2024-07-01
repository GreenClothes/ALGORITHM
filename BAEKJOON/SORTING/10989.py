# https://www.acmicpc.net/problem/10989

import sys

N = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    N[int(sys.stdin.readline())] += 1
for i in range(10001):
    if N[i] != 0:
        for j in range(N[i]):
            print(i)