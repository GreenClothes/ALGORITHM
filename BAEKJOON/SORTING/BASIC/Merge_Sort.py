before_Sort = list(map(int, input().split()))
print('Before : ', end='')
print(' '.join(str(i) for i in before_Sort))
sorted = [0] * len(before_Sort)

def Merge(list, left, middle, right):
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

def Merge_Sort(list, left, right):
    if left < right:
        middle = (left + right) // 2

        Merge_Sort(list, left, middle)
        Merge_Sort(list, middle+1, right)
        Merge(list, left, middle, right)

Merge_Sort(before_Sort, 0, len(before_Sort)-1)
after_Sort = before_Sort
print('After : ', end='')
print(' '.join(str(i) for i in after_Sort))