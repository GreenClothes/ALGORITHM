# https://www.acmicpc.net/problem/2581

m = int(input())
n = int(input())
num_dict = {i:True for i in range(n+1)}
num_dict[1] = False

for i in range(2, n//2+1):
    if num_dict[i]:
        j = 2
        while i*j <= n:
            num_dict[i*j] = False
            j += 1

num_sum = 0
num_min = 0
for i in range(m, n+1):
    if num_dict[i]:
        num_sum += i
        if num_min == 0:
            num_min = i

if not num_sum:
    print('-1')
else:
    print(num_sum, num_min, sep='\n')