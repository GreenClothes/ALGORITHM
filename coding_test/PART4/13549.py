# https://www.acmicpc.net/problem/13549

from collections import deque
from sys import maxsize
N, K = map(int, input().split())
location = {i:maxsize for i in range(100001)}
location[N] = 0
q = deque()
q.append(N)

while q:
    qp = q.popleft()
    temp = location[qp]
    if qp == K:
        print(temp)
        break

    plus, sub, mul = qp + 1, qp - 1, 2 * qp
    if 100001 > plus >= 0 and location[plus] > location[qp] + 1:
        location[plus] = location[qp] + 1
    if 100001 > sub >= 0 and location[sub] > location[qp] + 1:
        location[sub] = location[qp] + 1
        q.append(sub)
    if 100001 > mul >= 0 and location[mul] > location[qp]:
        location[mul] = location[qp]
        q.append(mul)
