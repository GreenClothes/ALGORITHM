# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

cal = input().strip()
m_flag = 1
cal_list = []
num = 0
for i in range(len(cal)):
    try:
        num = num * 10 + int(cal[i])
    except:
        if m_flag == -1: cal_list.append(-num)
        else: cal_list.append(num)
        if cal[i] == '-': m_flag = -1
        num = 0
    if i == len(cal)-1:
        cal_list.append(m_flag * num)
print(sum(cal_list))