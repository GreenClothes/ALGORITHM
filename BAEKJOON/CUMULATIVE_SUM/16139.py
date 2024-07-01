# https://www.acmicpc.net/problem/16139

import sys

S = sys.stdin.readline().strip()
S_a = [[0] * 26]
S_a[0][ord(S[0]) - 97] = 1

for i in range(1, len(S)):
    S_a.append(S_a[-1][:])
    S_a[i][ord(S[i]) - 97] += 1

for i in range(int(sys.stdin.readline().strip())):
    s, start, end = list(sys.stdin.readline().strip().split())
    start, end = map(int, [start, end])
    if start == 0:
        print(S_a[end][ord(s)-97])
    else:
        print(S_a[end][ord(s)-97] - S_a[start-1][ord(s)-97])