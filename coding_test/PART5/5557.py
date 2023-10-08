# https://www.acmicpc.net/problem/5557

import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
value = [[0] * 21 for _ in range(N-1)]
value[0][N_list[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if value[i-1][j]:
            plus, minus = j+N_list[i], j-N_list[i]
            if plus < 21:
                value[i][plus] += value[i-1][j]
            if minus >= 0:
                value[i][minus] += value[i-1][j]
print(value[N-2][N_list[-1]])