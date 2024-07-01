before_Sort = list(map(int, input().split()))
print('Before : ', end='')
print(' '.join(str(i) for i in before_Sort))

def Bubble_Sort(list):
    if len(list) == 1:
        return list

    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

after_Sort = Bubble_Sort(before_Sort)
print('After : ', end='')
print(' '.join(str(i) for i in after_Sort))