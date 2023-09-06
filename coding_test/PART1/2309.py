# https://www.acmicpc.net/problem/2309

men = sorted([int(input()) for _ in range(9)])
sum_men = sum(men)

def find_men(m, sm):
    for i in range(9):
        for j in range(i+1, 9):
            if sm - m[i] - m[j] == 100:
                return [i, j]
not_men = find_men(men, sum_men)
for i in range(9):
    if i not in not_men:
        print(men[i])