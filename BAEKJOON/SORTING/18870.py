# https://www.acmicpc.net/problem/18870

import sys

sys.stdin.readline().strip()
X = list(map(int, sys.stdin.readline().strip().split()))
X_set = sorted(set(X))
X_dict = {i:x for x, i in enumerate(X_set)}
for x in X: print(X_dict.get(x), end=' ')