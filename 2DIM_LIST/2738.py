# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())
mat = []
for i in range(N*2):
    mat.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        print(mat[i][j] + mat[i+N][j], end=' ')
    if i != N-1: print()