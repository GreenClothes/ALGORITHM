# https://www.acmicpc.net/problem/1007

import sys, math
from itertools import combinations
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    xy = []
    x_sum, y_sum = 0, 0

    for _ in range(N):
        x, y = map(int, input().split())
        x_sum += x
        y_sum += y
        xy.append([x, y])

    min_vect = sys.maxsize
    comb_vect = list(combinations(xy, N//2))
    for sum_vect in comb_vect[:len(comb_vect)//2]:
        sum_x, sum_y = 0, 0
        for sx, sy in sum_vect:
            sum_x += sx
            sum_y += sy
        sub_x = x_sum - sum_x
        sub_y = y_sum - sum_y

        min_vect = min(min_vect, math.sqrt((sum_x-sub_x)**2+(sum_y-sub_y)**2))
    print(min_vect)



