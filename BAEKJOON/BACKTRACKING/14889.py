# https://www.acmicpc.net/problem/14889

import sys

n = int(sys.stdin.readline().strip())
S = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visit = [False] * n
arr = []
p1 = [0]
p2 = []

def dfs():
    global p1, p2
    if len(p1) == n//2:
        for k in range(n):
            if k not in p1: p2.append(k)
        arr.append(abs(sum([S[x][y] for x in p1 for y in p1]) - sum([S[x][y] for x in p2 for y in p2])))
        p2 = []
        return


    for j in range(1, n):
        if j > p1[-1]:
            p1.append(j)
            dfs()
            p1.pop()
dfs()
print(min(arr))