# https://www.acmicpc.net/problem/2675

T = int(input())
for t in range(T):
    TestCase = str(input())
    R = int(TestCase[0])
    S = TestCase[2:]
    for s in range(len(S)):
        print(S[s]*R, end='')
    print()