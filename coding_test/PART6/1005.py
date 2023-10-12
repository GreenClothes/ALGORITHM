# https://www.acmicpc.net/problem/1005

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    XY = [[] for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        XY[y].append(x)
    W = int(input())
    time = [0] * (N+1)
    time[W] = D[W]
    q = deque([W])
    max_time = 0
    end = []

    while q:
        node = q.popleft()
        if XY[node]:
            for i in XY[node]:
                if time[i] < time[node] + D[i]:
                    time[i] = time[node] + D[i]
                    q.append(i)
        else:
            if time[node] > max_time:
                max_time = time[node]
    print(max_time)
