# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())
num_list = [1]
I = 2
while len(num_list) < b:
    for i in range(I):
        num_list.append(I+num_list[-1])
    I += 1
if a == 1:
    print(num_list[b-1])
else:
    print(num_list[b-1] - num_list[a-2])