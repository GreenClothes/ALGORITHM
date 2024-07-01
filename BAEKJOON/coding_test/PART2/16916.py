# https://www.acmicpc.net/problem/16916

import sys
input = sys.stdin.readline

S = input()
P = input()

def get_pi(string):
    pi = [0] * (len(string)-1)
    j = 0
    for s in range(1, len(string)):
        while j > 0 and string[s] != string[j]:
            j = pi[j-1]
        if string[s] == string[j]:
            j += 1
            pi[s] = j
    return pi

def KMP(PI):
    idx_p = 0
    idx_s = 0
    while idx_s < len(S):
        if S[idx_s] != P[idx_p]:
            idx_p = PI[idx_p-1]
        idx_s += 1
        idx_p += 1
        if idx_p == len(P)-1:
            return 1
    return 0

print(KMP(get_pi(P)))