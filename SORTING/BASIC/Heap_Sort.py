before_Sort = list(map(int, input().split()))
print('Before : ', end='')
print(' '.join(str(i) for i in before_Sort))

def Heapify(list, end):
    for i in range(end):
        child = i
        while child > 0:
            root = (child-1)//2
            if list[root] < list[child]:
                temp = list[root]
                list[root] = list[child]
                list[child] = temp
            child = root
    return list

def Heap_Sort(list):
    list = Heapify(list, len(list))

    for i in range(len(list)-1, 0, -1):
        temp = list[0]
        list[0] = list[i]
        list[i] = temp
        list = Heapify(list, i)

    return list

after_Sort = Heap_Sort(before_Sort)
print('After : ', end='')
print(' '.join(str(i) for i in after_Sort))