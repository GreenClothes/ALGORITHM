# https://www.acmicpc.net/problem/1629

import sys
input = sys.stdin.readline

# A, B, C = map(int, input().strip().split())
# ans = 1
# for _ in range(B):
#     ans = ans*A%C
# print(ans)
# print(10**5%12)
# 10%12 12
# 10**2%12
start = 1
for i in range(21):
    print(i, ':', end=' ')
    print(3**i%17, end=' ')
    print('predict :', start)
    start = start*3%17
# 17/3 = 5 --- 2
# 3 + 14 = 17
# 9 + 8 = 17
# 27 - 10 = 17 = 17 * 1 = 3**3
# 81 - 13 = 68 = 17 * 4 = 3**4
# 243 - 5 = 238 = 17 * 14 = 3**5
# 729 - 15 = 714 = 17 * 42 = 3**6
# A**B%C = ans
#
# (A**B+ans)/C = 몫
# A**B+ans = C
# C-A**B = ans