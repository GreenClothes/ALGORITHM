# https://www.acmicpc.net/problem/2023

N = int(input())
NUM = 10**(N-1)
first = [2, 3, 5, 7]

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def dfs(n):
    if n >= NUM:
        print(n)
        return

    for i in [1, 3, 7, 9]:
        num = n * 10 + i
        if isPrime(num):
            dfs(num)
for i in first:
    dfs(i)