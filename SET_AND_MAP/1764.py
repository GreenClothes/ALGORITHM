# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
N_name = set(input().strip() for _ in range(N))
M_name = set(input().strip() for _ in range(M))

NM_name = sorted(N_name & M_name)

print(len(NM_name))
print(*NM_name, sep='\n')