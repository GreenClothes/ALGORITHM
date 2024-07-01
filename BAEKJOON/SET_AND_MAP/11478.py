# https://www.acmicpc.net/problem/11478

import sys
input = sys.stdin.readline

S = input().strip()
s = set()
for ls in range(1, len(S)+1):
    for i in range(len(S)+1-ls):
        s.add(S[i:i+ls])
print(len(s))