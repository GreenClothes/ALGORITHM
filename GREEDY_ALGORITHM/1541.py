# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

cal = input().strip()
cal_list = []
num = 0
num_10 = 1
for i in range(len(cal)-1, -1, -1):
    try:
        num += int(cal[i])*num_10
        num_10 *= 10
    except:
        cal_list.insert(0, num)
        num = 0; num_10 = 1
        cal_list.insert(0, cal[i])
    if i==0:
        cal_list.insert(0, num)

for i in range(len(cal_list)):
    