# https://www.acmicpc.net/problem/1037

import sys
input = sys.stdin.readline

N = int(input().strip())
n = list(map(int, input().strip().split()))
if N != 1:
    print(max(n) * min(n))
else:
    print(n[0]**2)