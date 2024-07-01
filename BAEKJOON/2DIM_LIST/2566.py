# https://www.acmicpc.net/problem/2566

mat = []
n, m, maximum = 0, 0, 0
for i in range(9):
    mat.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if mat[i][j] > maximum:
            maximum = mat[i][j]
            n = i; m = j
print(maximum)
print(n+1, m+1, sep=' ')