# https://www.acmicpc.net/problem/9470

import sys
input = sys.stdin.readline

T = int(input())

def dfs(node):
    temp = []
    for i in range(M):
        if graph[node][i]:
            if not Strahler[i]:
                dfs(i)
            temp.append(Strahler[i])
    if len(temp) > 0:
        temp = sorted(temp)
        temp_cnt = temp.count(temp[-1])
        if temp_cnt > 1:
            Strahler[node] = temp[-1] + 1
        else:
            Strahler[node] = temp[-1]
    else:
        Strahler[node] = 1

for _ in range(T):
    K, M, P = map(int, input().split())
    graph = [[0] * M for _ in range(M)]
    for _ in range(P):
        a, b = map(int, input().split())
        graph[b-1][a-1] = 1
    Strahler = [0] * M

    for i in range(M):
        if not Strahler[i]:
            dfs(i)
    print(K, Strahler[-1])


