# https://www.acmicpc.net/problem/16113

import sys
input = sys.stdin.readline

N = int(input())
signal = list(input().strip())
sl = N//5
signal_solve = [signal[i*sl:(i+1)*sl] for i in range(5)]
num_dict = {('#', '#', '#', '.', '#', '#') : 0, ('#', '.', '#', '#', '#', '.') : 2, ('#', '.', '#', '#', '.', '#') : 3,
            ('.', '#', '#', '#', '.', '#') : 4, ('#', '#', '.', '#', '.', '#') : 5, ('#', '#', '.', '#', '#', '#') : 6,
            ('#', '.', '#', '.', '.', '#') : 7, ('#', '#', '#', '#', '#', '#') : 8, ('#', '#', '#', '#', '.', '#') : 9}
ans = []

def check_one(row):
    if row == sl-1:
        ans.append(1)
        return True
    else:
        for j in range(5):
            if signal_solve[j][row+1] == '#':
                return False
        ans.append(1)
        return True

i = 0

while i < sl:
    if signal_solve[0][i] == '#':
        if not check_one(i):
            ans.append(num_dict[(signal_solve[0][i+1], signal_solve[1][i], signal_solve[1][i+2], signal_solve[2][i+1],
                                 signal_solve[3][i], signal_solve[3][i+2])])
            i += 2
    i += 1
print(*ans, sep='')

