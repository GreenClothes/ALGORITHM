# https://www.acmicpc.net/problem/3036

import sys
input = sys.stdin.readline

N = int(input().strip())
R = list(map(int, input().strip().split()))
ans = []

def max_div(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def rotate(R, i, over, under):
    if i == len(R)-1: return

    GCD = max_div(R[i]*over, R[i+1]*under)
    over = R[i]*over//GCD
    under = R[i+1]*under//GCD
    ans.append([over, '/', under])
    return rotate(R, i+1, over, under)

rotate(R, 0, 1, 1)
for i in range(len(ans)):
    print(*ans[i], sep='')