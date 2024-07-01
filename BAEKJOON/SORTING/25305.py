# https://www.acmicpc.net/problem/25305

N, k = map(int, input().split())
print(sorted(list(map(int, input().split())))[-k])