# https://www.acmicpc.net/problem/2775

T = int(input())
for t in range(T):
    k = int(input()); n = int(input())
    house = [i+1 for i in range(n)]
    for K in range(k):
        for N in range(n):
            if N != 0:
                house[N] = house[N] + house[N-1]
    print(house[n-1])