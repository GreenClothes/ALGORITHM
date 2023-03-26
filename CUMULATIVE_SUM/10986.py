# https://www.acmicpc.net/problem/10986

import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
A[0] %= M

for i in range(1, N):
    A[i] = (A[i-1] + A[i]) % M
A = Counter(A)
ans = A[0]
for a in A.values():
    ans += a * (a-1) // 2
print(ans)