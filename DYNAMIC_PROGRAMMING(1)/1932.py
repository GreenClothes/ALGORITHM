# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

n = int(input().strip())
triangle = [list(map(int, input().strip().split())) for _ in range(n)]

def sum_triangle(n):
    for i in range(n-1, 0, -1):
        for j in range(len(triangle[i-1])):
            triangle[i-1][j] = max(triangle[i][j]+triangle[i-1][j], triangle[i][j+1]+triangle[i-1][j])

sum_triangle(n)
print(triangle[0][0])