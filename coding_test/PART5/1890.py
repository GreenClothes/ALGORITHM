# https://www.acmicpc.net/problem/1890

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
way = [[0]*N for _ in range(N)]
way[0][0] = 1

for i in range(N):
    for j in range(i, N):
        if i == N-1 and j == N-1:
            break
        if way[i][j]:
            dr, dc = board[i][j] + j, board[i][j] + i
            if N > dr:
                way[i][dr] += way[i][j]
            if N > dc:
                way[dc][j] += way[i][j]
        if i != j:
            if way[j][i]:
                dr, dc = board[j][i] + i, board[j][i] + j
                if N>dr:
                    way[j][dr] += way[j][i]
                if N>dc:
                    way[dc][i] += way[j][i]
print(way[N-1][N-1])