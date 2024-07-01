# https://www.acmicpc.net/problem/5622

S = list(str(input()))
sum = 0
for s in S:
    num = (ord(s)-64)
    if num <= 3: sum += 3
    elif num <= 6: sum += 4
    elif num <= 9: sum += 5
    elif num <= 12: sum += 6
    elif num <= 15: sum += 7
    elif num <= 19: sum += 8
    elif num <= 22: sum += 9
    else: sum += 10
print(sum)