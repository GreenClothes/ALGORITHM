# https://www.acmicpc.net/problem/1022

import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())
ans = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
max_num = 0

def find(y, x):
    seq = max(abs(x), abs(y))
    if x <= y:
        return (seq*2+1)**2 - (seq-y) - (seq-x)
    else:
        return (seq*2)**2 - (y+seq) - (x+seq-1)

for r in range(r2-r1+1):
    for c in range(c2-c1+1):
        ans[r][c] = find(r+r1, c+c1)
        max_num = max(ans[r][c], max_num)

max_num = len(str(max_num))
for r in range(r2-r1+1):
    for c in range(c2-c1+1):
        print(str(ans[r][c]).rjust(max_num), end=' ')
    print()