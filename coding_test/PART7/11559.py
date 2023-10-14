# https://www.acmicpc.net/problem/11559

import sys
from collections import deque
input = sys.stdin.readline

field = [[] for _ in range(6)]
for i in range(12):
    s = list(input().strip())
    for j in range(6):
        field[j].append(s[j])
cnt = 0

def bfs():
    visited = [[False] * 12 for _ in range(6)]
    r = False
    q = deque()
    for i in range(12):
        for j in range(6):
            if field[j][i] != '.' and not visited[j][i]:
                puyo_tmp = []
                puyo = field[j][i]
                q.append((j, i))
                puyo_tmp.append((j, i))
                visited[j][i] = True
                while q:
                    y, x = q.popleft()
                    for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        dy += y
                        dx += x
                        if 0 <= dy < 6 and 0 <= dx < 12 and puyo == field[dy][dx] and not visited[dy][dx]:
                            visited[dy][dx] = True
                            q.append((dy, dx))
                            puyo_tmp.append((dy, dx))
                if len(puyo_tmp) >= 4:
                    for py, px in puyo_tmp:
                        field[py][px] = '.'
                    r = True
    return r

def set_PUYO():
    for i in range(6):
        for j in range(12):
            if field[i][j] == '.':
                del field[i][j]
                field[i].insert(0, '.')

while bfs():
    set_PUYO()
    cnt += 1
print(cnt)

