# https://www.acmicpc.net/problem/2609

n, m = map(int, input().split())

def max_div(a, b):
    while b!=0:
        a, b = b, a%b
        if b == 0:
            return a
md = max_div(n, m)

print(md, n*m//md, sep='\n')