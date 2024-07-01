# https://www.acmicpc.net/problem/7568

import sys

n = int(sys.stdin.readline().strip())
N = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]
rank = [1] * n

for i in range(n):
    for j in range(n):
        if N[i][0] < N[j][0] and N[i][1] < N[j][1]: rank[i] += 1

print(*rank, sep=' ')