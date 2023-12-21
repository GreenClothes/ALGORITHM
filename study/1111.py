# https://www.acmicpc.net/problem/1111

import sys
input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))

def pattern(cnt, numbers):
    if cnt == 1:
        return 'A'
    if cnt == 2:
        if numbers[0] == numbers[1]:
            return numbers[0]
        else:
            return 'A'

    if numbers[0] == numbers[1]:
        a = 1
    else:
        a = (numbers[2]-numbers[1])/(numbers[1]-numbers[0])
        if a % 1:
            return 'B'

    b = numbers[1] - numbers[0] * a
    for c in range(1, cnt-1):
        if numbers[c] * a + b != numbers[c+1]:
            return 'B'
    return int(numbers[-1] * a + b)

print(pattern(N, n))