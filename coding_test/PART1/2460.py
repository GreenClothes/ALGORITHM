# https://www.acmicpc.net/problem/2460

train_dict = {n:list(map(int, input().split())) for n in range(10)}
people = 0
people_max = 0
for n in range(10):
    people += (train_dict[n][1] - train_dict[n][0])
    if people > people_max:
        people_max = people
print(people_max)