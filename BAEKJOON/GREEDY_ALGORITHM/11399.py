# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

N = int(input().strip())
P = sorted(list(map(int, input().strip().split())))
P_sum = P[0]

for i in range(1, N):
    P[i] = P[i-1] + P[i]
    P_sum += P[i]
print(P_sum)