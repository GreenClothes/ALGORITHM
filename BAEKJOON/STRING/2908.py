# https://www.acmicpc.net/problem/2908

a, b = map(str, input().split())
a = int(a[::-1])
b = int(b[::-1])
if a >= b:
    print(a)
else:
    print(b)