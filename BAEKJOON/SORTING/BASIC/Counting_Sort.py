before_Sort = list(map(int, input().split()))
print('Before : ', end='')
print(' '.join(str(i) for i in before_Sort))

def Counting_Sort(list):
    c_list = [0 for i in range(max(list)+1)]
    for i in list:
        c_list[i] += 1

    r_list = [i for i in range(len(c_list)) for j in range(c_list[i])]

    return r_list

after_Sort = Counting_Sort(before_Sort)
print('After : ', end='')
print(' '.join(str(i) for i in after_Sort))