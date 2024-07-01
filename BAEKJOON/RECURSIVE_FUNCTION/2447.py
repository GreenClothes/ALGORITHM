# https://www.acmicpc.net/problem/2447

import sys

def STAR(n):
    if n == 1: return [['*']]

    first = second = third = star_pix = STAR(n//3)
    for i in range(2):
        first = list(map(list.__add__, first, star_pix))
        third = list(map(list.__add__, third, star_pix))
    for i in range(2):
        if i == 0: second = list(map(list.__add__, second, [[' ']*(n//3)]*(n//3)))
        else: second = list(map(list.__add__, second, star_pix))

    return first + second + third

S = STAR(int(sys.stdin.readline().strip()))
for n in range(len(S)):
    print(*S[n], sep='')