# https://www.acmicpc.net/problem/1789

S = int(input())
num_dict = {i:i for i in range(1, int((2*S)**(1/2))+2)}
for i in range(1, len(num_dict)+2):
    if num_dict[i] > S:
        print(i-1)
        break
    num_dict[i+1] += num_dict[i]