# https://www.acmicpc.net/problem/2580

from timeit import default_timer as timer
from datetime import timedelta
import sys

sudoku = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
start = timer()

zero = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0: zero.append([i, j])

def not_in_num(x, y, val):
    for i in range(9):
        if val == sudoku[y][i] or val == sudoku[i][x] or val == sudoku[y//3*3 + i//3][x//3*3 + i%3]:
            return False
    return True

def SUDOKU(i):

    if i == len(zero):
        for k in range(9):
            print(*sudoku[k])
        exit(0)

    for j in range(1, 10):
        x = zero[i][1]
        y = zero[i][0]

        if not_in_num(x, y, j):
            sudoku[y][x] = j
            SUDOKU(i+1)
            sudoku[y][x] = 0

SUDOKU(0)


end = timer()
print(timedelta(seconds=end - start))
'''
0 0 0 0 0 0 0 0 9
0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 0 7
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 4
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 1
'''