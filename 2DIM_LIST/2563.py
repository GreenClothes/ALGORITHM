# https://www.acmicpc.net/problem/2563

paper = [[1]*100 for _ in range(100)]
black = []
for i in range(int(input())):
    black.append(list(map(int, input().split())))
for i in range(len(black)):
    for j in range(10):
        for k in range(10):
            paper[black[i][0]+j][black[i][1]+k] = 0
white = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 0: white += 1
print(white)