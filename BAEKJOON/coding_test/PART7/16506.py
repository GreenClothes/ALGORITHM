# https://www.acmicpc.net/problem/16506

import sys
input = sys.stdin.readline

N = int(input())
command = [list(input().split()) for _ in range(N)]

command_dict = {'ADD':['0000', '0', '', '', ''], 'SUB':['0001', '0', '', '', ''], 'MOV':['0010', '0', '', '', ''],
                'AND':['0011', '0', '', '', ''], 'OR':['0100', '0', '', '', ''], 'NOT':['0101', '0', '', '', ''],
                'MULT':['0110', '0', '', '', ''], 'LSFTL':['0111', '0', '', '', ''], 'LSFTR':['1000', '0', '', '', ''],
                'ASFTR':['1001', '0', '', '', ''], 'RL':['1010', '0', '', '', ''], 'RR':['1011', '0', '', '', '']}
for c in command:
    if c[0][-1] == 'C':
        op = command_dict[c[0][:-1]].copy()
        op[0] += '1'
        op[4] = str(format(int(c[3]), 'b')).rjust(4, '0')
    else:
        op = command_dict[c[0]].copy()
        op[0] += '0'
        op[4] = str(format(int(c[3]), 'b')).rjust(3, '0') + '0'

    op[2] = str(format(int(c[1]), 'b')).rjust(3, '0')
    op[3] = str(format(int(c[2]), 'b')).rjust(3, '0')

    print(*op, sep='')