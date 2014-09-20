def PerkalianMatriks(A, B):
    baris_a = len(a)
    baris_b = len(b)
    C = [[0 for y in range(baris_b)] for x in range(baris_a)]

    for i in range(0, baris_a):
        for j in range(0, baris_b):
            C[i][j] = 0

            for k in range(0, baris_a):
                C[i][j] = C[i][j] + (A[i][k] * B[k][j])

    return C
