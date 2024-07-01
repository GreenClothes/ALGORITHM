# https://www.acmicpc.net/problem/2693

T = int(input())
for t in range(T):
    print(sorted(list(map(int, input().split())))[-3])