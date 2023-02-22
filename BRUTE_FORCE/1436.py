# https://www.acmicpc.net/problem/1436

import sys

N = int(sys.stdin.readline().strip())
num_666 = 0
num = 666

while N != 0:
    cnt_6 = 0
    for n in str(num):
        if n == '6': cnt_6 += 1
        else: cnt_6 = 0
        if cnt_6 == 3:
            num_666 = num
            N -= 1
    num += 1

print(num_666)