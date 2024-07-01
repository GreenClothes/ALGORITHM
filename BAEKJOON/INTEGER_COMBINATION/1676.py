# https://www.acmicpc.net/problem/1676

import sys, math

N = str(math.factorial(int(sys.stdin.readline().strip())))
ans = 0
for i in range(1, len(N)+1):
    if N[-i] != '0':
        ans = i-1
        break
print(ans)