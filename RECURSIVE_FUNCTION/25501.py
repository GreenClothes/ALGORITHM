# https://www.acmicpc.net/problem/25501

import sys

def recursion(s, l, r):
    STR[i][1] += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

STR = [[0, 0]+[sys.stdin.readline().strip()] for _ in range(int(sys.stdin.readline().strip()))]
for i in range(len(STR)):
    STR[i][0] = isPalindrome(STR[i][2])
    print(STR[i][0], STR[i][1])