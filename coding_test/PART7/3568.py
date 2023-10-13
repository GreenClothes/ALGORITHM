# https://www.acmicpc.net/problem/3568

import sys
from collections import deque
input = sys.stdin.readline

S = deque(list(input().strip()))
struct = ''
stack = []

Sp = S.popleft()
while Sp != ' ':
    struct += Sp
    Sp = S.popleft()

while S:
    s = S.popleft()
    if s == ',' or s == ';':
        print(struct, end='')
        for _ in range(len(stack)):
            print(stack.pop(), end='')
        print()
    elif s != ' ':
        if 'a' <= s <= 'z' or 'A' <= s <= 'Z':
            while 'a' <= S[0] <= 'z' or 'A' <= S[0] <= 'Z':
                s += S.popleft()
            s = ' ' + s + ';'
        if s == '[':
            s += S.popleft()
        stack.append(s)
