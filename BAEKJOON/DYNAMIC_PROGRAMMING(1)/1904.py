# https://www.acmicpc.net/problem/1904

import sys

tiles = []

def tile(N):
    tiles.append(1)
    tiles.append(2)

    for i in range(2, N):
        tiles.append((tiles[i-1] + tiles[i-2])%15746)

N = int(sys.stdin.readline().strip())
tile(N)
print(tiles[N-1])
