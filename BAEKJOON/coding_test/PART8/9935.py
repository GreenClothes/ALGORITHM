# https://www.acmicpc.net/problem/9935

import sys
input = sys.stdin.readline

S = list(input().strip())
boom = list(input().strip())
boom_len = len(boom)
stack = []

for s in S:
    stack.append(s)
    if len(stack) >= boom_len:
        if stack[-boom_len:] == boom:
            for j in range(boom_len):
                stack.pop()

if len(stack) > 0:
    print(*stack, sep='')
else:
    print('FRULA')

