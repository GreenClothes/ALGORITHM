# https://www.acmicpc.net/problem/1197

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(E)]
tree = sorted(tree, key=lambda x:x[2])
parent = {i:i for i in range(1, V+1)}
cost = []

def find_parent(k):
    if parent[k] == k: return k
    parent[k] = find_parent(parent[k])
    return parent[k]

for t in tree:
    t0_parent, t1_parent = find_parent(t[0]), find_parent(t[1])
    if t1_parent != t0_parent:
        if t0_parent < t1_parent:
            parent[t1_parent] = t0_parent
        else:
            parent[t0_parent] = t1_parent
        cost.append(t[2])
    if len(cost) == V-1:
        break
print(sum(cost))