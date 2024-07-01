# https://www.acmicpc.net/problem/1112

import sys
input = sys.stdin.readline

x, b = map(int, input().split())
pos = 1 if b < 0 or (x >= 0 and b >= 0) else 0
x = x if pos else -x
ans = []
while x:
    y, z = divmod(x, b)
    if z < 0:
        y += 1
        z -= b
    x = y
    ans.append(z)
if ans:
    print(*ans[::-1], sep='') if pos else print('-', *ans[::-1], sep='')
else:
    print(0)