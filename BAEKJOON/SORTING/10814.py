# https://www.acmicpc.net/problem/10814

import sys

N = sorted([list(sys.stdin.readline().strip().split()+[i]) for i in range(int(sys.stdin.readline().strip()))], key=lambda x: x[2])
N = sorted(N, key=lambda x: int(x[0]))
for i in range(len(N)): print(N[i][0], N[i][1])