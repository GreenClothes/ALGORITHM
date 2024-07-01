# https://www.acmicpc.net/problem/2108

import sys

N = sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])
X = [0] * 8001
for n in N:
    X[n+4000] +=1
mode = [max(X)]
for i in range(len(X)):
    if X[i] == mode[0]:
        mode.append(i)
        if len(mode) == 3:
            mode.remove(mode[1])
            break
print(round(sum(N)/len(N)), N[len(N)//2], mode[1]-4000, max(N)-min(N), sep='\n')