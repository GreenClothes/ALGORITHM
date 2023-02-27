# https://www.acmicpc.net/problem/1002

import sys
input = sys.stdin.readline

for i in range(int(input().strip())):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    if dx == 0 and dy == 0 and r1 == r2:
        print('-1')
    elif dx**2+dy**2 > (r1+r2)**2 or dx**2+dy**2 < abs(r1-r2)**2:
        print('0')
    elif dx**2+dy**2 == (r1+r2)**2 or dx**2+dy**2 == abs(r1-r2)**2:
        print('1')
    else:
        print('2')