def CekPrima(n):
    prima = True
    for i in range(2, n):
        if n % i == 0:
            prima = False

    return prima
