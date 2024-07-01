before_Sort = list(map(int, input().split()))
print('Before : ', end='')
print(' '.join(str(i) for i in before_Sort))

def Quick_Sort(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list)//2]
    left = [i for i in list if i < pivot]
    middle = [i for i in list if i == pivot]
    right = [i for i in list if i > pivot]

    return Quick_Sort(left) + middle + Quick_Sort(right)

after_Sort = Quick_Sort(before_Sort)
print('After : ', end='')
print(' '.join(str(i) for i in after_Sort))