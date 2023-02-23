# https://www.acmicpc.net/problem/3009

import sys
input = sys.stdin.readline
x, y = [], []

for i in range(3):
    X, Y = map(int, input().strip().split())

    if X in x: x.remove(X)
    else: x.append(X)
    if Y in y: y.remove(Y)
    else: y.append(Y)

print(x[0], y[0])