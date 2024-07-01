# https://www.acmicpc.net/problem/2290

import sys
input = sys.stdin.readline

s, n = input().strip().split()
s = int(s)
len_S = len(n)
num_dict = {'0':['-', '|', '|', ' ', '|', '|', '-'], '1':[' ', ' ', '|', ' ', ' ', '|', ' '],
            '2':['-', ' ', '|', '-', '|', ' ', '-'], '3':['-', ' ', '|', '-', ' ', '|', '-'],
            '4':[' ', '|', '|', '-', ' ', '|', ' '], '5':['-', '|', ' ', '-', ' ', '|', '-'],
            '6':['-', '|', ' ', '-', '|', '|', '-'], '7':['-', ' ', '|', ' ', ' ', '|', ' '],
            '8':['-', '|', '|', '-', '|', '|', '-'], '9':['-', '|', '|', '-', ' ', '|', '-']}

for num in n:
    print(' ', end='')
    for r in range(s):
        print(num_dict[num][0], end='')
    print('  ', end='')
print()
for c in range(s):
    for num in n:
        print(num_dict[num][1], end='')
        for r in range(s):
            print(' ', end='')
        print(num_dict[num][2], end=' ')
    print()
for num in n:
    print(' ', end='')
    for r in range(s):
        print(num_dict[num][3], end='')
    print('  ', end='')
print()
for c in range(s):
    for num in n:
        print(num_dict[num][4], end='')
        for r in range(s):
            print(' ', end='')
        print(num_dict[num][5], end=' ')
    print()
for num in n:
    print(' ', end='')
    for r in range(s):
        print(num_dict[num][6], end='')
    print('  ', end='')