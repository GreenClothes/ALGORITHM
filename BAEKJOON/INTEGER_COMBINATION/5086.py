# https://www.acmicpc.net/problem/5086

import sys
input = sys.stdin.readline

while 1:
    x, y = map(int, input().strip().split())
    if x == 0 and y == 0: break

    xdivy = x % y
    ydivx = y % x
    if ydivx == 0:
        print('factor')
    elif xdivy == 0:
        print('multiple')
    else:
        print('neither')