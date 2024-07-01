# https://www.acmicpc.net/problem/8911

import sys
input = sys.stdin.readline

T = int(input())
d_y = [1, 0, -1, 0]
d_x = [0, -1, 0, 1]

for _ in range(T):
    control = list(input().strip())
    d = 0
    yx = [0, 0]
    max_y, min_y = 0, 0
    max_x, min_x = 0, 0
    for c in control:
        if c == 'F':
            yx[0] += d_y[d]
            yx[1] += d_x[d]
        elif c == 'B':
            yx[0] -= d_y[d]
            yx[1] -= d_x[d]
        elif c == 'L':
            if d == 0: d = 3
            else: d -= 1
        elif c == 'R':
            if d == 3: d = 0
            else: d += 1
        max_y = max(max_y, yx[0])
        min_y = min(min_y, yx[0])
        max_x = max(max_x, yx[1])
        min_x = min(min_x, yx[1])
    print((max_y-min_y)*(max_x-min_x))