# https://www.acmicpc.net/problem/10809

p = [-1 for i in range(26)]
S = input()
for i, j in enumerate(S):
    if p[ord(j)-97] == -1:
        p[ord(j) - 97] = i
for P in p:
    print(P, end=' ')