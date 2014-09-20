def SelectionSort(A):
    n = len(A)

    for j in range(0, n - 1):
        imin = j
        for i in range(j + 1, n):
            if (A[i] < A[imin]):
                imin = i

        A[imin], A[j] = A[j], A[imin]
