# https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
w = list(map(int, input().split()))
ans = 0
m_w = max(w)

for i in range(1, W-1):
    if w[i] != m_w:
        ans += (min(max(w[:i+1]), max(w[i:]))-w[i])

print(ans)