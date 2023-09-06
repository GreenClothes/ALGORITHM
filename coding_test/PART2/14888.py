# https://www.acmicpc.net/problem/14888

N = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
ans = []

def cal(num, i):
    global add, sub, mul, div
    if i == N-1:
        ans.append(num)
        return

    if add:
        add -= 1
        cal(num+num_list[i+1], i+1)
        add += 1
    if sub:
        sub -= 1
        cal(num-num_list[i+1], i+1)
        sub += 1
    if mul:
        mul -= 1
        cal(num*num_list[i+1], i+1)
        mul += 1
    if div:
        div -= 1
        if num < 0: cal(-(abs(num)//num_list[i+1]), i+1)
        else: cal(num//num_list[i+1], i+1)
        div += 1

cal(num_list[0], 0)
print(max(ans), min(ans), sep='\n')