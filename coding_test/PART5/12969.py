# https://www.acmicpc.net/problem/12969

N, K = map(int, input().split())
dp = [[[[False] * 435 for _ in range(31)] for _ in range(31)] for _ in range(31)]
S = ['' for _ in range(N)]

def find(idx, a, b, k):
    if idx == N:
        if k == K:
            print(*S, sep='')
            exit()
        else:
            return False
    if dp[idx][a][b][k]:
        return False
    dp[idx][a][b][k] = True

    S[idx] = 'A'
    find(idx+1, a+1, b, k)
    S[idx] = 'B'
    find(idx+1, a, b+1, k+a)
    S[idx] = 'C'
    find(idx+1, a, b, k+a+b)

    return False
find(0, 0, 0, 0)
print(-1)