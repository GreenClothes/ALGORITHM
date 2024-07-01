# https://www.acmicpc.net/problem/2504

string = input()

def pair_check(s):
    stack = []
    pair = {')': '(', ']': '['}
    tmp = 1
    ans = 0

    for i in range(len(s)):
        if s[i] in pair:
            if not stack or stack[-1] != pair[s[i]]:
                return 0
            p = stack.pop()
            if p == '(':
                if s[i-1] == p:
                    ans += tmp
                tmp //= 2
            else:
                if s[i-1] == p:
                    ans += tmp
                tmp //= 3
        else:
            if s[i] == '(':
                tmp *= 2
            else:
                tmp *= 3
            stack.append(s[i])
    if stack: return 0
    else: return ans

print(pair_check(string))
