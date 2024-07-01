# https://www.acmicpc.net/problem/2234

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(M)]
map = [[[] for _ in range(N)] for _ in range(M)]
for i in range(M):
    for j in range(N):
        room = wall[i][j]
        if not room & 1:
            map[i][j].append([i, j-1])
        if not room & 2:
            map[i][j].append([i-1, j])
        if not room & 4:
            map[i][j].append([i, j+1])
        if not room & 8:
            map[i][j].append([i+1, j])
q = deque()
visited = [[False] * N for _ in range(M)]
cnt = 0
size = []
max_size = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            stack = []
            sz = 0
            q.append([i, j])
            stack.append([i, j])
            visited[i][j] = True
            while q:
                sz += 1
                qp = q.popleft()
                qi, qj = qp[0], qp[1]
                for room in map[qi][qj]:
                    if not visited[room[0]][room[1]]:
                        visited[room[0]][room[1]] = True
                        q.append(room)
                        stack.append(room)
            cnt += 1
            size.append(sz)
            visited_tmp = [[False] * N for _ in range(M)]
            while stack:
                st = stack.pop()
                for di, dj in [(-1, 0), (0, 1), (1, 0), (1, 0)]:
                    di += st[0]
                    dj += st[1]
                    if M > di >= 0 and N > dj >= 0:
                        if [di, dj] not in map[st[0]][st[1]] and not visited[di][dj] and not visited_tmp[di][dj]:
                            q.append([di, dj])
                            visited_tmp[di][dj] = True
                            sz = 0
                            while q:
                                sz += 1
                                qp = q.popleft()
                                qi, qj = qp[0], qp[1]
                                for room in map[qi][qj]:
                                    if not visited[room[0]][room[1]] and not visited_tmp[room[0]][room[1]]:
                                        visited_tmp[room[0]][room[1]] = True
                                        q.append(room)
                            max_size = max(max_size, size[-1] + sz)
print(cnt)
print(max(size))
print(max_size)
