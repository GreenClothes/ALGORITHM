# https://www.acmicpc.net/problem/2587

N = sorted([int(input()) for _ in range(5)])
print(sum(N)//len(N), N[len(N)//2], sep='\n')