# https://www.acmicpc.net/problem/1193

N = int(input())
times = 1
while N > times:
    N -= times
    times += 1
print(N, times)
up, down = 1, times
for n in range(N-1):
    up += 1
    down -= 1
if times%2 == 1:
    print(down, '/', up, sep='')
else:
    print(up, '/', down, sep='')