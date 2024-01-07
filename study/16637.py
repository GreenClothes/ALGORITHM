# https://www.acmicpc.net/problem/16637

import sys
input = sys.stdin.readline

N = int(input())
calc = input()
ans = []

def CALC(result, n):
    if n >= N:
        ans.append(int(result))
        return

    if n+4 <= N:
        CALC(str(eval(result+calc[n]+str(eval(calc[n+1:n+4])))), n+4)
    if n+2 <= N:
        CALC(str(eval(result+calc[n:n+2])), n+2)
CALC(calc[0], 1)
print(max(ans))