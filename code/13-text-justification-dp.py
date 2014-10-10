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

    line = 1
    while n > 1:
        print("line " + str(line) + ": " + str(s[n]) + "->" + str(n))
        n = s[n] - 1
        line += 1

    return s

string = "Tristique augue auctor amet turpis integer nunc dapibus pellentesque turpis scelerisque penatibus, lacus nascetur cum quis, turpis nascetur mauris turpis, augue platea nunc, tincidunt placerat quis nec? Adipiscing turpis? Platea, aenean dignissim cum scelerisque placerat pulvinar! Hac placerat urna tincidunt. Dapibus mid! Lacus augue purus ridiculus integer aliquam, mauris pid hac pellentesque. Phasellus tortor, facilisis tristique nisi sed porta cum eros. Habitasse elementum? Pulvinar! Sit tincidunt in cursus enim dignissim purus rhoncus? Habitasse, lundium porttitor elit nec nisi ac nascetur porta cum adipiscing pulvinar, vel vel adipiscing porttitor dis nisi, aliquam turpis, natoque nec magnis, porttitor urna turpis magnis! Aenean! Urna augue, cras nisi, cras magna turpis eu duis proin porttitor dis magna duis, aliquam, sit elementum a nunc? Nec."
s = break_line(string, 80)

