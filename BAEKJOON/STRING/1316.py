# https://www.acmicpc.net/problem/1316

N = int(input())
g_num = N
for n in range(N):
    S = input()
    buf = []
    for s in S:
        if s not in buf:
            buf.append(s)
        elif buf[-1] == s:
            continue
        else:
            g_num -= 1
            break
print(g_num)