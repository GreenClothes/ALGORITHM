# https://www.acmicpc.net/problem/1085

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().strip().split())
distance = [x, y, w-x, h-y]
print(min(distance))