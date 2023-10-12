# https://www.acmicpc.net/problem/2533

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
visited = {i:False for i in range(1, N+1)}
child = [False] * (N+1)

def dfs(node):
    if visited[node]:
        return False
    visited[node] = True

    for i in tree[node]:
        if dfs(i):
            if not child[i] and not child[node]:
                child[node] = True
    return True

dfs(1)
print(child.count(True))