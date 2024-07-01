# https://www.acmicpc.net/problem/1934

import sys
input = sys.stdin.readline

def max_div(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def min_mul(a, b):
    return (a * b) // max_div(a, b)

for i in range(int(input().strip())):
    A, B = map(int, input().strip().split())
    print(min_mul(A, B))