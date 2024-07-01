# https://www.acmicpc.net/problem/2981

import sys
input = sys.stdin.readline

N = [int(input().strip()) for _ in range(int(input().strip()))]
N.sort()
M = [N[i+1]-N[i] for i in range(len(N)-1)]

def max_div(a, b):
    while b != 0:
        a, b = b, a%b
    return a

GCD = M[0]
for i in range(len(M)-1):
    GCD = max_div(GCD, M[i+1])
ans = set()
for i in range(2, int(GCD**0.5)+1):
    if GCD%i == 0:
        ans.add(i)
        ans.add(GCD//i)
ans.add(GCD)
print(*sorted(list(ans)))