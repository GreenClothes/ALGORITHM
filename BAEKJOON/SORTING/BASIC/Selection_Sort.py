before_Sort = list(map(int, input().split()))
print('Before : ', end='')
print(' '.join(str(i) for i in before_Sort))

def Selection_Sort(list):
    for i in range(len(list)):
        min = list[i]
        index = i
        for j in range(i, len(list)):
            if list[j] < min:
                min = list[j]
                index = j
        temp = list[index]
        list[index] = list[i]
        list[i] = temp
    return list

after_Sort = Selection_Sort(before_Sort)
print('After : ', end='')
print(' '.join(str(i) for i in after_Sort))
