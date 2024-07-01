# https://www.acmicpc.net/problem/2178

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append([0, 0])

def bfs():
    global cnt
    while q:
        qp = q.popleft()
        if qp[0] == N-1 and qp[1] == M-1:
            return

        for i in range(4):
            di, dj = qp[0] + dy[i], qp[1] + dx[i]
            if N > di >= 0 and M > dj >= 0 and maze[di][dj] == '1':
                if visited[di][dj] == 0 or visited[qp[0]][qp[1]] + 1 < visited[di][dj]:
                    visited[di][dj] = visited[qp[0]][qp[1]] + 1
                    q.append([di, dj])
bfs()
print(visited[N-1][M-1])