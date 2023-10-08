# https://www.acmicpc.net/problem/11058

N = int(input())
dp = [i for i in range(N+1)]

for i in range(6, N+1):
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4, dp[i-6]*5)

print(dp[N])