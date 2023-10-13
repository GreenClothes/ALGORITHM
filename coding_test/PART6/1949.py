# https://www.acmicpc.net/problem/1949

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
people = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visited = {i:False for i in range(1, N+1)}
dp = [[0, 0] for _ in range(N+1)]

def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = people[node]

    for t in tree[node]:
        if visited[t]:
            continue
        dfs(t)
        dp[node][0] += max(dp[t][0], dp[t][1])
        dp[node][1] += dp[t][0]
dfs(1)
print(max(dp[1][0], dp[1][1]))