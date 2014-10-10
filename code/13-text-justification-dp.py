def length(word_lengths, i, j):
    return sum(word_lengths[i- 1:j]) + j - i + 1


def break_line(text, L):
    # wl = lengths of words
    wl = [len(word) for word in text.split()]

    # n = number of words in the text
    n = len(wl)
    print(n)

    # total badness of a text l1 ... li
    m = dict()
    m[0] = 0    

    s = dict()

    for i in range(1, n + 1):
        sums = dict()
        k = i
        while (length(wl, k, i) <= L and k > 0):
            # badness calculation
            sums[(L - length(wl, k, i))**3 + m[k - 1]] = k
            k -= 1
        m[i] = min(sums)
        s[i] = sums[min(sums)]

    return s

