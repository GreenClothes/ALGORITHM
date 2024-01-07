# https://www.acmicpc.net/problem/1132

import sys
input = sys.stdin.readline

N = int(input())
nums = [[0, False] for _ in range(10)]
ans = 0
for _ in range(N):
    S = input().strip()
    m = 1
    nums[ord(S[0])-65][1] = True
    for s in range(len(S)-1, -1, -1):
        nums[ord(S[s])-65][0] += m
        m *= 10
nums = sorted(nums, reverse=True)

if nums[9][1]:
    for i in range(8, -1, -1):
        if not nums[i][1]:
            del nums[i]
            break
for i in range(9):
    ans += nums[i][0] * (9-i)

print(ans)