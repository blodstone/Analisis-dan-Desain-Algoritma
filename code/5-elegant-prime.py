def CekPrima(n):
    res = [False if n % x == 0 else True for x in range(2, n)]
    return not False in res

