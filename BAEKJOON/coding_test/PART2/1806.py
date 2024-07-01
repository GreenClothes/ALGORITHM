# https://www.acmicpc.net/problem/1806

N, S = map(int, input().split())
NUMS = list(map(int, input().split()))
idx = []

if sum(NUMS) < S:
    print(0)
elif sum(NUMS) == S:
    print(N)
else:
    left, right = 0, 0
    sum_NUMS = 0
    for n in range(N):
        sum_NUMS += NUMS[n]
        if sum_NUMS >= S:
            for m in range(left, n+1):
                if sum_NUMS - NUMS[m] < S:
                    idx.append(n-m+1)
                    break
                sum_NUMS -= NUMS[m]
                left += 1
    print(min(idx))