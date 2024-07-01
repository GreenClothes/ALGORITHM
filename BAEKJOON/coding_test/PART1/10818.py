# https://www.acmicpc.net/problem/10818

N = int(input())
Ns = sorted(list(map(int, input().split())))
print(Ns[0], Ns[-1])