# https://www.acmicpc.net/problem/14238

S = list(input())
A, B, C = 0, 1, 2
cnt = [S.count(s) for s in ('A', 'B', 'C')]
dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(len(S))]for _ in range(len(S))]for _ in range(len(S))]
ans = [''] * len(S)

def permute(a, b, c, prev):
    if [a, b, c] == cnt:
        print(''.join(ans))
        exit()
    if dp[a][b][c][prev[0]][prev[1]]:
        return False
    dp[a][b][c][prev[0]][prev[1]] = True
    if a + 1 <= cnt[A]:
        ans[a+b+c] = 'A'
        if permute(a+1, b, c, [prev[1], A]):
            return True
    if b + 1 <= cnt[B]:
        ans[a+b+c] = 'B'
        if prev[1] != B:
            if permute(a, b+1, c, [prev[1], B]):
                return True
    if c + 1 <= cnt[C]:
        ans[a + b + c] = 'C'
        if prev[0] != C and prev[1] != C:
            if permute(a, b, c+1, [prev[1], C]):
                return True
    return False
permute(0, 0, 0, [0, 0])
print(-1)