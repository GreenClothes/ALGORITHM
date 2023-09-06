# https://www.acmicpc.net/problem/10870

n = int(input())
fib_dict = {0:0, 1:1, 2:1}
for i in range(n+1):
    if i in fib_dict:
        continue
    else:
        fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
print(fib_dict[n])