# https://www.acmicpc.net/problem/2798

import sys

N, M = map(int, sys.stdin.readline().strip().split())
card = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse=True)
min = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card[i] + card[j] + card[k]
            if sum <= M and sum > min:
                min = sum
print(min)