# https://www.acmicpc.net/problem/2839

N = int(input())
box = []
for count_5 in range(1001):
    if count_5 * 5 > N:
        break
    count_3 = (N - 5 * count_5) // 3
    if N - 5 * count_5 - 3 * count_3 == 0:
        box.append(count_5 + count_3)
try:
    print(min(box))
except:
    print('-1')