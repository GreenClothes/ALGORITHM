# https://www.acmicpc.net/problem/2616

import sys
input = sys.stdin.readline

train = int(input())
people = list(map(int, input().split()))
carry = int(input())
people_sum = [0]
for i in range(train):
    people_sum.append(people_sum[i]+people[i])
dp = [[0 for _ in range(train+1)] for _ in range(3)]

for i in range(3):
    for j in range(i*carry, train+1):
        if i == 0:
            dp[i][j] = max(dp[i][j-1], people_sum[j] - people_sum[j-carry])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-carry]+people_sum[j]-people_sum[j-carry])

print(dp[-1][-1])