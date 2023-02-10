before_Sort = list(map(int, input().split()))
print('Before : ', end='')
print(' '.join(str(i) for i in before_Sort))

def Insert_Sort(list):
    if len(list) != 1 and len(list) != 0:
        for i in range(1, len(list)):
            j = i
            while list[j] < list[j-1] and j != -1:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
                j -= 1
            print(list)
    return list

after_Sort = Insert_Sort(before_Sort)
print('After : ', end='')
print(' '.join(str(i) for i in after_Sort))