# https://www.acmicpc.net/problem/2281

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
people = [int(input()) for _ in range(n)]
dp = [sys.maxsize] * n
dp[n-1] = 0

def note(idx):
    if dp[idx] < sys.maxsize:
        return dp[idx]

    blank = m - people[idx]
    for i in range(idx+1, n+1):
        if i == n:
            dp[idx] = 0
            break
        dp[idx] = min(dp[idx], blank**2+note(i))
        blank -= (people[i]+1)
        if blank < 0:
            break
    return dp[idx]

print(note(0))