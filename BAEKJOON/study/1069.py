# https://www.acmicpc.net/problem/1069

import sys, math
input = sys.stdin.readline

X, Y, D, T = map(int, input().split())
distance = math.sqrt(X**2+Y**2)
time = min(distance, distance-distance//D*D+distance//D*T)
time = min(time, (distance//D+1)*D-distance+(distance//D+1)*T)
if distance//D > 0:
    time = min(time, (distance//D+1)*T)
else:
    time = min(time, T*2)
print(time)
