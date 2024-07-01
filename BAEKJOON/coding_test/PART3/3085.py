# https://www.acmicpc.net/problem/3085

import sys
input = sys.stdin.readline

N = int(input())
candy = [list(input()) for _ in range(N)]

def swap(a, b):
    return b, a

def cnt_candy(x, y):
    row_max, col_max = 1, 1
    for c in range(N):
        row_cnt = 1
        for m in range(1, N):
            if candy[c][m] == candy[c][m-1]:
                row_cnt += 1
            else:
                row_cnt = 1
            if row_cnt > row_max:
                row_max = row_cnt
    for r in range(N):
        col_cnt = 1
        for n in range(1, N):
            if candy[n][r] == candy[n-1][r]:
                col_cnt += 1
            else:
                col_cnt = 1
            if col_cnt > col_max:
                col_max = col_cnt

    return row_max if row_max > col_max else col_max

dx = [0, 1]
dy = [1, 0]
result = 1
for i in range(N):
    for j in range(N):
        for k in range(2):
            di, dj = i+dy[k], j+dx[k]
            if N>di>=0 and N>dj>=0 and candy[di][dj] != candy[i][j]:
                candy[di][dj], candy[i][j] = swap(candy[di][dj], candy[i][j])
                cnt = cnt_candy(j, i)
                candy[di][dj], candy[i][j] = swap(candy[di][dj], candy[i][j])
                if cnt > result: result = cnt
print(result)