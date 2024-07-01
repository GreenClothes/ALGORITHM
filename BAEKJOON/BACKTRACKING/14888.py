# https://www.acmicpc.net/problem/14888

from timeit import default_timer as timer
from datetime import timedelta
import sys
input = sys.stdin.readline

n = int(input().strip())
N = list(map(int, input().strip().split()))
add, sub, mul, div = map(int, input().strip().split())
ans = []

start = timer()


def comb_cal(i, val):
    global add, sub, mul, div

    if i == n-1:
        ans.append(val)
        return
    else:
        if add > 0:
            add -= 1
            comb_cal(i+1, val+N[i+1])
            add += 1
        if sub > 0:
            sub -= 1
            comb_cal(i+1, val-N[i+1])
            sub += 1
        if mul > 0:
            mul -= 1
            comb_cal(i+1, val*N[i+1])
            mul += 1
        if div > 0:
            div -= 1
            if val < 0: comb_cal(i+1, -(abs(val)//N[i+1]))
            else: comb_cal(i+1, val//N[i+1])
            div += 1

comb_cal(0, N[0])
print(max(ans), min(ans), sep='\n')

end = timer()
print(timedelta(seconds=end - start))