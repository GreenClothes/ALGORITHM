# https://www.acmicpc.net/problem/6987

import sys
from itertools import combinations
input = sys.stdin.readline

def dfs(round):
    global cnt

    if round == 15:
        cnt = 1
        for sub in WTL_list:
            if sub.count(0) != 3:
                cnt = 0
                break
        return

    g1, g2 = games[round]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if WTL_list[g1][x] > 0 and WTL_list[g2][y] > 0:
            WTL_list[g1][x] -= 1
            WTL_list[g2][y] -= 1
            dfs(round + 1)
            WTL_list[g1][x] += 1
            WTL_list[g2][y] += 1


answers = []
games = list(combinations(range(6), 2))

for _ in range(4):
    WTL = list(map(int, input().split()))
    WTL_list = [WTL[i:i + 3] for i in range(0, 16, 3)]
    cnt = 0
    dfs(0)
    answers.append(cnt)

print(*answers)
