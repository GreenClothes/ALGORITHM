# https://www.acmicpc.net/problem/12026

N = int(input())
block = list(input())
dp = [1000001] * N
visited = {i:False for i in range(N)}
dp[0] = 0
visited[0] = True
match = {'B':'J', 'O':'B', 'J':'O'}

for i in range(1, N):
    m = match[block[i]]
    for j in range(i):
        if m == block[j]:
            dp[i] = min(dp[i], dp[j] + (i-j)**2)

            if dp[i] != 1000001:
                visited[i] = True
if visited[N-1]:
    print(dp[N-1])
else:
    print(-1)