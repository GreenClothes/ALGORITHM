# https://www.acmicpc.net/problem/2292

N = int(input()) - 1
rooms = 1
while 1:
    N = N - (6 * rooms - 6)
    if N <= 0:
        break
    rooms += 1
print(rooms)