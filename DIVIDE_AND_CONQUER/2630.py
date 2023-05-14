# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

N = int(input().strip())
P = [list(map(int, input().strip().split())) for _ in range(N)]
num_paper = []

def DC(x, y, n):
    c = P[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if c != P[i][j]:
                DC(x, y, n//2)
                DC(x+n//2, y, n//2)
                DC(x, y+n//2, n//2)
                DC(x+n//2, y+n//2, n//2)
                return
    num_paper.append(c)

DC(0, 0, N)
print(num_paper.count(0))
print(num_paper.count(1))