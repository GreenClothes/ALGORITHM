# https://www.acmicpc.net/problem/2941

S = input()
c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in c_alpha:
    if c in S:
        S = S.replace(c, ' ')
print(len(S))