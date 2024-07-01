# https://www.acmicpc.net/problem/11050

import sys, math

N, K = map(int, sys.stdin.readline().strip().split())
print(math.factorial(N)//(math.factorial(K)*math.factorial(N-K)))