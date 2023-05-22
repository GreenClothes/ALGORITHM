# https://www.acmicpc.net/problem/1992

import sys
input = sys.stdin.readline

N = int(input().strip())
Q = [input().strip() for _ in range(N)]
ans = ['(']

def DC(x, y, n):
    img = Q[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if img != Q[i][j]:
                # 영상 압축 순서 생각해보기
                ans.append('(')
                DC(x, y, n // 2)
                DC(x + n // 2, y, n // 2)
                DC(x, y + n // 2, n // 2)
                DC(x + n // 2, y + n // 2, n // 2)
                ans.append(')')
                return
    ans.append(img)

DC(0, 0, N)
print(*ans)