# https://www.acmicpc.net/problem/1978

num = int(input())
N = list(map(int, input().split()))
for n in N:
    if n == 1: num -= 1
    elif n != 2:
        for i in range(2, n//2+1):
            if n % i == 0:
                num -= 1
                break
print(num)