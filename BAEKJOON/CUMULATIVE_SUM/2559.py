# https://www.acmicpc.net/problem/2559

import sys

N, K = map(int, sys.stdin.readline().strip().split())
temp = list(map(int, sys.stdin.readline().strip().split()))
temp_con = []
temp_con.append(sum(temp[:K]))

for i in range(N-K):
    temp_con.append(temp_con[i] - temp[i] + temp[i+K])

print(max(temp_con))