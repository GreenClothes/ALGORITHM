# https://www.acmicpc.net/problem/15486

import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []
benefit = {i:0 for i in range(0, N+1)}
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
max_b = 0

for i in range(N-1, -1, -1):
    if T[i]+i <= N:
        benefit[i] = max(benefit[T[i]+i]+P[i], max_b)
        max_b = benefit[i]
    else:
        benefit[i] = max_b
print(max(benefit.values()))