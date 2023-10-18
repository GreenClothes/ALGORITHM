# https://www.acmicpc.net/problem/4949

import sys
input = sys.stdin.readline

S = []
s = input().rstrip()
S.append(s)
pair = {']':'[', ')':'('}
while s != '.':
    s = input().rstrip()
    if s[-1] == '.' and S[-1][-1] == '.':
        S.append(s)
    else:
        S[-1] += s

def check(c):
    stack = []
    for s in c:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ']' or s == ')':
            if len(stack) == 0:
                print('no')
                return
            elif stack[-1] != pair[s]:
                print('no')
                return
            stack.pop()
    if len(stack) > 0:
        print('no')
    else:
        print('yes')

for i in range(len(S)-1):
    check(S[i])
