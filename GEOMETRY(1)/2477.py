# https://www.acmicpc.net/problem/2477

import sys
input = sys.stdin.readline

cnt = int(input().strip())
area = [list(map(int, input().strip().split())) for _ in range(6)]

max_val_w, max_val_h, max_idx_w, max_idx_h = 0, 0, 0, 0
for i in range(6):
    if area[i][1] > max_val_w and (area[i][0] == 1 or area[i][0] == 2):
        max_val_w = area[i][1]
        max_idx_w = i
    if area[i][1] > max_val_h and (area[i][0] == 3 or area[i][0] == 4):
        max_val_h = area[i][1]
        max_idx_h = i
piece_w = abs(area[(max_idx_h - 1)%6][1] - area[(max_idx_h + 1)%6][1])
piece_h = abs(area[(max_idx_w - 1)%6][1] - area[(max_idx_w + 1)%6][1])
print(cnt * (max_val_h * max_val_w - piece_h * piece_w))
