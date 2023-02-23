# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
poke_dict = {'{0}'.format(i+1):input().strip() for i in range(N)}
poke_dict_inv = {v:k for k, v in poke_dict.items()}
for m in range(M):
    Q = input().strip()
    try:
        print(poke_dict[Q])
    except Exception:
        print(poke_dict_inv[Q])