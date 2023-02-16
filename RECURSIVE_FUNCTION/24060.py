# https://www.acmicpc.net/problem/24060

import sys

N, K = map(int, sys.stdin.readline().strip().split())
list = list(map(int, sys.stdin.readline().strip().split()))
K_SAVE = 0
sorted = [0] * len(list)

def Merge(list, left, middle, right):
    global K, K_SAVE
    i = left; j = middle+1; sort_list_idx = left

    while i<=middle and j<=right:
        if list[i] <= list[j]:
            sorted[sort_list_idx] = list[i]
            sort_list_idx += 1; i += 1
        else:
            sorted[sort_list_idx] = list[j]
            sort_list_idx += 1; j += 1
    if i > middle:
        for k in range(j, right+1):
            sorted[sort_list_idx] = list[k]
            sort_list_idx += 1
    else:
        for k in range(i, middle+1):
            sorted[sort_list_idx] = list[k]
            sort_list_idx += 1

    for k in range(left, right+1):
        list[k] = sorted[k]
        K -= 1
        if K == 0: K_SAVE = sorted[k]

def Merge_Sort(list, left, right):
    if left < right:
        middle = (left + right) // 2

        Merge_Sort(list, left, middle)
        Merge_Sort(list, middle+1, right)
        Merge(list, left, middle, right)

Merge_Sort(list, 0, len(list)-1)
print(K_SAVE if K_SAVE != 0 else '-1')

