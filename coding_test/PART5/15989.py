# https://www.acmicpc.net/problem/15989

import sys
input = sys.stdin.readline

T = int(input())
n = [int(input()) for _ in range(T)]
max_n = max(n)
n_dict = {i:1 for i in range(max_n+1)}

for i in range(2, max_n+1):
    n_dict[i] += n_dict[i-2]
for i in range(3, max_n+1):
    n_dict[i] += n_dict[i-3]

for t in range(T):
    print(n_dict[n[t]])