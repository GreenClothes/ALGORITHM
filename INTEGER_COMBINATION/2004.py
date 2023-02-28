# https://www.acmicpc.net/problem/2004

import sys

n, m = map(int, sys.stdin.readline().strip().split())

def count_2(i):
    cnt = 0
    while i != 0:
        i = i//2
        cnt += i
    return cnt

def count_5(i):
    cnt = 0
    while i != 0:
        i = i//5
        cnt += i
    return cnt

print(min(count_2(n) - count_2(n-m) - count_2(m), count_5(n) - count_5(n-m) - count_5(m)))