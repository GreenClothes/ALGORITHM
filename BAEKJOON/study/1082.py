# https://www.acmicpc.net/problem/1082

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
M = int(input())
if N == 1:
    print(0)
else:
    min_not0 = min(P[1:])
    if min_not0 > M:
        print(0)
        exit()
    min_0 = min(P)
    num = []
    num.append(P.index(min_not0))
    M -= min_not0
    for _ in range(M//min_0):
        num.append(P.index(min_0))
    M -= M//min_0*min_0

    for i in range(len(num)):
        for j in range(N-1, -1, -1):
            if P[j]-P[num[i]] <= M:
                num[i] = j
                if i == 0:
                    M -= (P[j] - min_not0)
                else:
                    M -= (P[j] - min_0)
                break
    print(*num, sep='')

