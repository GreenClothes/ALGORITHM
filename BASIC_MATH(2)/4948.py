# https://www.acmicpc.net/problem/4948

N = []
N.append(int(input()))
while N[-1] != 0:
    N.append(int(input()))
prime = [i for i in range(2*max(N)+1)]
cnt_prime = [0 for i in range(len(N)-1)]
for i in range(2, len(prime)):
    j = 2
    while i * j < len(prime):
        prime[i * j] = 1
        j += 1
for i in range(len(N)-1):
    for j in range(N[i]+1, 2*N[i]+1):
        if prime[j] != 1:
            cnt_prime[i] += 1
for c in cnt_prime:
    print(c)