# https://www.acmicpc.net/problem/1834

N = int(input())
num_sum = 0
for i in range(1, N):
    num_sum += (N*i+i)
print(num_sum)