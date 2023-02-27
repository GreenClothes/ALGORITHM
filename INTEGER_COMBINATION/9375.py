# https://www.acmicpc.net/problem/9375

import sys
input = sys.stdin.readline

for i in range(int(input().strip())):
    cloth = dict()
    for j in range(int(input().strip())):
        _, type = input().strip().split()
        if type in cloth:
            cloth[type] += 1
        else:
            cloth[type] = 1

    ans = 1
    for j in cloth.values():
        ans *= (j+1)
    print(ans-1)