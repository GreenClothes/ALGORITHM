# https://www.acmicpc.net/problem/1141

import sys
input = sys.stdin.readline

N = int(input())
S = set()
for _ in range(N):
    S.add(input().strip())
S = list(S)
size = len(S)

for i in range(len(S)):
    for j in range(len(S)):
        i_len = len(S[i])
        if len(S[j]) > i_len:
            if S[i] == S[j][:i_len]:
                size -= 1
                break
print(size)


