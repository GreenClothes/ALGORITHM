# https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
cnt_dict = {i:0 for i in range(k+1)}
cnt_dict[0] = 1

for c in coins:
    for i in range(c, k+1):
        cnt_dict[i] = cnt_dict[i] + cnt_dict[i-c]
print(cnt_dict[k])

