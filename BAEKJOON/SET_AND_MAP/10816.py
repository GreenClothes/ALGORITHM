# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

input()
N = list(map(int, input().strip().split()))
M_len = int(input().strip())
M = list(map(int, input().strip().split()))
M_cnt = []

N_dict = dict()
for n in N:
    if n in N_dict:
        N_dict[n] += 1
    else:
        N_dict[n] = 1

for m in M:
    if m in N_dict: M_cnt.append(N_dict[m])
    else: M_cnt.append(0)

print(*M_cnt, sep=' ')