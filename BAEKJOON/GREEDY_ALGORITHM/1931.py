# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

N = int(input().strip())
M_t = sorted(list(map(int, input().strip().split())) for _ in range(N))
M = [M_t[0]]

for n in range(1, N):
    if M_t[n][1] < M[-1][1]:
        M.pop()
        M.append(M_t[n])
    elif M_t[n][0] >= M[-1][1]:
        M.append(M_t[n])
print(len(M))