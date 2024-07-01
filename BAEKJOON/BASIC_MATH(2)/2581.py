# https://www.acmicpc.net/problem/2581

M = int(input()); N = int(input())
sum, min = 0, 0
for i in range(M, N+1):
    if i == 2: min = 2; sum += i
    elif i != 1:
        sum += i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                sum -= i
                break
            if j == i//2 and min == 0:
                min = i
if min == 0: print('-1')
else: print(sum, min, sep='\n')