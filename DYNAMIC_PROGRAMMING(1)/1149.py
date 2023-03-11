# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

N = int(input().strip())
house = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(1, N):
    house[i][0] = min(house[i][0] + house[i-1][1], house[i][0] + house[i-1][2])
    house[i][1] = min(house[i][1] + house[i-1][0], house[i][1] + house[i-1][2])
    house[i][2] = min(house[i][2] + house[i-1][0], house[i][2] + house[i-1][1])

print(min(house[-1]))