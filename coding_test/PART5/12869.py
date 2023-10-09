# https://www.acmicpc.net/problem/12869

import sys
input = sys.stdin.readline

N = int(input())
health = list(map(int, input().split()))
health.extend([0, 0])
dp = [[[61] * 61 for _ in range(61)] for _ in range(61)]
attack = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
atk = 7*7*7

def mutal(x, y, z):
    global atk
    if not(x or y or z):
        atk = min(atk, dp[x][y][z])
        return

    for a in range(6):
        i, j, k = attack[a]
        dx, dy, dz = x - i, y - j, z - k
        if dx < 0: dx = 0
        if dy < 0: dy = 0
        if dz < 0: dz = 0

        if dp[dx][dy][dz] > dp[x][y][z] + 1:
            dp[dx][dy][dz] = dp[x][y][z] + 1
            mutal(dx, dy, dz)
dp[health[0]][health[1]][health[2]] = 0
mutal(health[0], health[1], health[2])
print(atk)