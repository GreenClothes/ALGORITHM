# https://www.acmicpc.net/problem/1269

import sys
input = sys.stdin.readline

input().strip().split()
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

Sym_diff_AB = (A | B) - (A & B)
print(len(Sym_diff_AB))