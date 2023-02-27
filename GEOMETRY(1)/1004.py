# https://www.acmicpc.net/problem/1004

import sys
input = sys.stdin.readline

for i in range(int(input().strip())):
    x1, y1, x2, y2 = map(int, input().strip().split())
    planet = [list(map(int, input().strip().split())) for _ in range(int(input().strip()))]

    inout = 0
    for p in planet:
        if (abs(p[0]-x1)**2 + abs(p[1]-y1)**2 > p[2]**2 and abs(p[0]-x2)**2 + abs(p[1]-y2)**2 > p[2]**2) or (abs(p[0] - x1) ** 2 + abs(p[1] - y1) ** 2 < p[2]**2 and abs(p[0] - x2) ** 2 + abs(p[1] - y2) ** 2 < p[2]**2):
            pass
        else:
            inout += 1
    print(inout)