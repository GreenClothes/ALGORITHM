# https://www.acmicpc.net/problem/9663

import sys
from timeit import default_timer as timer
from datetime import timedelta

start = timer()

N = int(sys.stdin.readline().strip())
queen_col = [0] * N
ans = 0

def poss_position(n, value):
    for k in range(n):
        if value == queen_col[k] or abs(value - queen_col[k]) == n-k:
            return False
    return True

def Queen(i, col):
    global ans

    if i == N:
        ans += 1
    else:
        for j in range(N):
            col[i] = j
            if poss_position(i, col[i]):
                Queen(i+1, col)

Queen(0, queen_col)
print(ans)
end = timer()
print(timedelta(seconds=end - start))