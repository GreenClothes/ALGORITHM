# https://www.acmicpc.net/problem/1062

N, K = map(int, input().split())
word = [input() for _ in range(N)]
max_word = 0


def word_check(k, n, c):
    global max_word

    if k == 0:
        cnt = 0
        for l in range(N):
            if (word_bit[l] & c) == word_bit[l]:
                cnt += 1
        if cnt > max_word:
            max_word = cnt
        return

    for l in range(n, 26):
        if (c & (1 << l)) == 0:
            c |= (1 << l)
            word_check(k-1, l, c)
            c &= ~(1 << l)


if K < 4:
    print(0)
elif K == 26:
    print(len(word))
else:
    word_bit = [0] * N
    for i in range(N):
        for w in word[i]:
            word_bit[i] |= 1 << (ord(w) - ord('a'))

    check = 0
    check |= 1 << (ord('a') - ord('a'))
    check |= 1 << (ord('c') - ord('a'))
    check |= 1 << (ord('i') - ord('a'))
    check |= 1 << (ord('n') - ord('a'))
    check |= 1 << (ord('t') - ord('a'))

    word_check(K-5, 0, check)

    print(max_word)




