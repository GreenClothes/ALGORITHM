# https://www.acmicpc.net/problem/24416

import sys

def fibonacci_RF(n):
    global ans_RF

    if n == 1 or n == 2:
        ans_RF += 1
        return 0
    else: return fibonacci_RF(n-1) + fibonacci_RF(n-2)

def fibonacci_DP(n):
    global ans_DP

    for i in range(3, n+1):
        ans_DP += 1

ans_RF = 0
ans_DP = 0
n = int(sys.stdin.readline().strip())
fibonacci_RF(n)
fibonacci_DP(n)
print(ans_RF, ans_DP, sep=' ')