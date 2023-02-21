# https://www.acmicpc.net/problem/11729

import sys

def HANOI(n, move, other, to):
    if n == 1:
        print(move, to)
        return

    HANOI(n-1, move, to, other)
    print(move, to)
    HANOI(n-1, other, move, to)

N = int(sys.stdin.readline().strip())
print(2**N-1)
HANOI(N, 1, 2, 3)