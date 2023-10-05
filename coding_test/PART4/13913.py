# https://www.acmicpc.net/problem/13913

from collections import deque
N, K = map(int, input().split())
location = {i:-1 for i in range(100001)}
q = deque()
q.append((N, 0))
location[N] = N
path = []

while q:
    n, t = q.popleft()
    if n == K:
        idx = n
        while idx != N:
            path.append(idx)
            idx = location[idx]
        path.append(N)
        print(t)
        break
    if n+1 < 100001 and location[n+1] == -1:
        q.append((n+1, t+1))
        location[n+1] = n
    if n-1 >= 0 and location[n-1] == -1:
        q.append((n-1, t+1))
        location[n-1] = n
    if 2*n < 100001 and location[2*n] == -1:
        q.append((2*n, t+1))
        location[2*n] = n

print(*path[::-1])