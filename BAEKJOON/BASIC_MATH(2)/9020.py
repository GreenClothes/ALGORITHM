# https://www.acmicpc.net/problem/9020

N = [int(input()) for i in range(int(input()))]
prime = [i for i in range(max(N))]
ans = []
for i in range(2, len(prime)):
    j = 2
    while i * j < len(prime):
        prime[i * j] = 1
        j += 1
for n in N:
    for i in range(n//2):
        if prime[n//2-i] != 1 and prime[n//2+i] != 1:
            ans.append(prime[prime.index(n//2-i)])
            ans.append(prime[prime.index(n//2+i)])
            break
for i in range(len(ans)//2):
    print(ans[2*i], ans[2*i+1], sep=' ')