# https://www.acmicpc.net/problem/10844

import sys

N = int(sys.stdin.readline().strip())
n = [1]*10
n[0] = 0

for i in range(1, N):
    temp = [0]*10
    temp[0] = n[1]
    temp[9] = n[8]
    for j in range(1, 9):
        temp[j] = n[j-1] + n[j+1]
    n = temp
print(sum(n)%1000000000)