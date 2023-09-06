# https://www.acmicpc.net/problem/3460

T = int(input())
n = {t:int(input()) for t in range(T)}

for t in range(T):
    i = 0
    while n[t]:
        if n[t] % 2:
            print(i, end=' ')
        n[t] >>= 1
        i += 1
    print()