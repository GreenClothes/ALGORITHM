# https://www.acmicpc.net/problem/1978

N = int(input())
n = sorted(list(map(int, input().split())))
nm = n[-1]

n_dict = {i:True for i in range(1, nm+1)}
n_dict[1] = False


for i in range(1, nm//2):
    if n_dict[i]:
        j = 2
        while i*j <= nm:
            n_dict[i*j] = False
            j += 1

cnt = 0
for i in n:
    if n_dict[i]:
        cnt += 1
print(cnt)