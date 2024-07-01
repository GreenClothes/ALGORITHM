# https://www.acmicpc.net/problem/9461

import sys

def triangle(N):
    triangles.append(1)
    triangles.append(1)
    triangles.append(1)
    triangles.append(2)
    triangles.append(2)

    for i in range(5, N):
        triangles.append(triangles[i-1] + triangles[i-5])

for i in range(int(sys.stdin.readline().strip())):
    triangles = []
    N = int(sys.stdin.readline().strip())
    triangle(N)
    print(triangles[N-1])