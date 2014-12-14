import collections
from bisect import bisect_left, bisect_right

def create_suffixArray(t):
    suffixes = {}
    for i in range(len(t)):
        suffixes[t[i:]] = i
    suffixes = collections.OrderedDict(sorted(suffixes.items()))
    return suffixes

def string_matching_naive(p, suffixes):
    foundIndex = []
    for k in suffixes:
        if p == k[0:len(p)]:
            foundIndex.append(suffixes[k])
    return foundIndex

def string_matching_bs(p, suffixes):
    foundIndex = []
    l_suffixes = list(suffixes)
    lo = 0
    hi = len(suffixes)-2
    mid = lo
    while(lo<hi):
        mid = (lo+hi)//2
        if p < l_suffixes[mid][:len(p)] or p == l_suffixes[mid][:len(p)]:
            hi = mid
        else:
            lo = mid + 1
    if p != l_suffixes[lo][:len(p)]:
        return [-1]
    first = lo
    lo = 0
    hi = len(suffixes)-2
    mid = lo
    while(lo<hi):
        mid = (lo+hi)//2
        if p < l_suffixes[mid][:len(p)]:
            hi = mid
        else:
            lo = mid + 1
    if p != l_suffixes[hi][:len(p)]:
        hi = hi - 1
    second = hi
    for i in range(first, second+1):
        foundIndex.append(suffixes[l_suffixes[i]])
    return foundIndex

def compute_LCP(suffixes):
    H = {}
    L_suffixes = list(suffixes)
    H[0] = 0
    for i in range(1,len(suffixes)):
        L = 0
        while(L_suffixes[i][L] == L_suffixes[i-1][L]):
            L = L + 1
        H[i] = L
    return H

t = 'banana$'
p = 'ab'

suffixes = create_suffixArray(t)
indexes_naive = string_matching_naive(p, suffixes)
indexes_bs = string_matching_bs(p, suffixes)
print(indexes_naive)
print(indexes_bs)
print(compute_LCP(suffixes))
