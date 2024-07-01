# https://www.acmicpc.net/problem/10250

T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1
    if floor == 0: floor = H; room -= 1
    print('{0}{1:02d}'.format(floor, room))