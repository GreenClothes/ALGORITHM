N, K = map(int, input().split())
measure_dict = dict()
for i in range(1, N//2):
    if i in measure_dict:
        break
    if N%i == 0:
        measure_dict[i] = True
        measure_dict[N//i] = True

measures = sorted(measure_dict.keys())
if len(measures) < K:
    print(0)
else:
    print(measures[K-1])