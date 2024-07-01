# https://www.acmicpc.net/problem/2609

import sys
N, M = map(int, input().strip().split())

def max_div(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def min_mul(a, b):
    return (a * b) // max_div(a, b)

print(max_div(N, M), min_mul(N, M), sep='\n')