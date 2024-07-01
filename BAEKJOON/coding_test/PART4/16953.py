# https://www.acmicpc.net/problem/16953

A, B = map(int, input().split())
cnt = 1
while A < B:
    if B % 10 == 1:
        B //= 10
        cnt += 1
    elif B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        print(-1)
        exit()
if A != B:
    print(-1)
else:
    print(cnt)