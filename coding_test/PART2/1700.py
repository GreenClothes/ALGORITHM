# https://www.acmicpc.net/problem/1700

N, K = map(int, input().split())
k = list(map(int, input().split()))
cnt = 0
multi = set()

for i, k_obj in enumerate(k):
    multi.add(k_obj)
    if len(multi) > N:
        latest = 0
        max_idx = -1
        for m in multi:
            try:
                num_idx = k[i:].index(m)
            except ValueError:
                num_idx = K
            if max_idx < num_idx:
                latest, max_idx = m, num_idx

        multi.discard(latest)
        cnt += 1
print(cnt)
