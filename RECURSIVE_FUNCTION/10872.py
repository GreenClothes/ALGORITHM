# https://www.acmicpc.net/problem/10872

import sys

def factorial(n):
    if n != 0:
        return n * factorial(n-1)
    else:
        return 1
print(factorial(int(sys.stdin.readline().strip())))