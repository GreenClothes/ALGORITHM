# https://www.acmicpc.net/problem/1157

S = list(str(input()).upper())
cnt = [0 for i in range(26)]
for s in S:
    cnt[ord(s)-65] += 1
m_cnt = max(cnt)
result = ''
for c in cnt:
    if m_cnt == c and result == '':
        result = chr(cnt.index(c)+65)
    elif m_cnt == c and result != '':
        result = '?'
        break
print(result)