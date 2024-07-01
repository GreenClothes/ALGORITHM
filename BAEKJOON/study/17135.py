# https://www.acmicpc.net/problem/17135

import sys
input = sys.stdin.readline

N, M, D = map(int, input().split())
if D > N:
    D = N
BOARD = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def shoot(a, b, c, go, B, dead):
    global ans
    if go == N:
        ans = max(ans, dead)
        return

    kill = dict()
    for d in range(1, D+1):
        for n in range(N-go-1, N-go-d-1, -1):
            for m in range(M):
                if abs(a-m) + abs(N-go-n) == d and B[n][m]:
                    if a not in kill:
                        kill[a] = [n, m, d]
                    elif kill[a][1] > m and kill[a][2] >= d:
                        kill[a] = [n, m, d]
                if abs(b-m) + abs(N-go-n) == d and B[n][m]:
                    if b not in kill:
                        kill[b] = [n, m, d]
                    elif kill[b][1] > m and kill[b][2] >= d:
                        kill[b] = [n, m, d]
                if abs(c-m) + abs(N-go-n) == d and B[n][m]:
                    if c not in kill:
                        kill[c] = [n, m, d]
                    elif kill[c][1] > m and kill[c][2] >= d:
                        kill[c] = [n, m, d]
        if len(kill) == 3:
            break
    for y, x, d in kill.values():
        if B[y][x]:
            dead += 1
            B[y][x] = 0
    for i in range(M):
        B[N-go-1][i] = 0
    shoot(a, b, c, go+1, B, dead)

for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            shoot(i, j, k, 0, [x[:] for x in BOARD], 0)
print(ans)

