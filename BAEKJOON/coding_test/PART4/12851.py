# https://www.acmicpc.net/problem/12851

from collections import deque
N, K = map(int, input().split())
location = {i:0 for i in range(100001)}
q = deque()
q.append(N)
cnt, temp = 0, 0

while q:
    qp = q.popleft()
    temp = location[qp]
    if qp == K:
        result = temp
        cnt += 1
        continue

    for i in [qp-1, qp+1, 2*qp]:
        if 100001 > i >= 0 and (location[i] == 0 or location[i] == location[qp] + 1):
            location[i] = location[qp] + 1
            q.append(i)
print(result, cnt, sep='\n')