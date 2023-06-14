# https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

N = int(input().strip())
P = [list(map(int, input().strip().split())) for _ in range(N)]
num_paper = []

def DC(x, y, n):
    p = P[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if p != P[i][j]:
                DC(x, y, n//3)
                DC(x+n//3, y, n//3)
                DC(x, y+n//3, n//3)
                DC(x+n//3, y+n//3, n//3)
                DC(x+n*2//3, y, n//3)
                DC(x, y+n*2//3, n//3)
                DC(x+n*2//3, y+n*2//3, n//3)
                DC(x+n*2//3, y+n//3, n//3)
                DC(x+n//3, y+n*2//3, n//3)
                return
    num_paper.append(p)

DC(0, 0, N)
print(num_paper.count(-1), num_paper.count(0), num_paper.count(1), sep='\n')