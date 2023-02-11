before_Sort = list(map(int, input().split()))
print('Before : ', end='')
print(' '.join(str(i) for i in before_Sort))

def Merge(list, left, middle, right):
    i = left; j = middle+1; sort_list_idx = left

    while i<=middle and j<=right:
        if list[i] <= list[j]:
            after_Sort[sort_list_idx] = list[i]
            sort_list_idx += 1; i += 1
        else:
            after_Sort[sort_list_idx] = list[j]
            sort_list_idx += 1; j += 1

        for k in range(i, middle+1):
            after_Sort[sort_list_idx] = list[k]
            sort_list_idx += 1
        for k in range(j, right):
            after_Sort[sort_list_idx] = list[k]

def Merge_Sort(list, left, right):
    middle = len(list) // 2

    if left < right:
        Merge_Sort(list, left, middle)
        Merge_Sort(list, middle+1, right)
        Merge(list, left, middle, right)

after_Sort = before_Sort
Merge_Sort(list, 0, len(before_Sort)-1)
print('After : ', end='')
print(' '.join(str(i) for i in after_Sort))