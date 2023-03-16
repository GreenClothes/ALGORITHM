# https://www.acmicpc.net/problem/11054

import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
dp1 = [1] * N
dp2 = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp = [dp1[i] + dp2[i] for i in range(N)]
print(max(dp)-1)