# https://www.acmicpc.net/problem/13305

import sys
input = sys.stdin.readline

N = int(input().strip())
L = list(map(int, input().strip().split()))
C = list(map(int, input().strip().split()))
min_cost = 1000000000
cost = 0

for i in range(N-1):
    if C[i] < min_cost: min_cost = C[i]
    cost += min_cost * L[i]
print(cost)