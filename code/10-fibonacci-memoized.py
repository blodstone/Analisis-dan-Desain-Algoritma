memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]

    if n <= 2:
        f = 1
    else:
        f = fibonacci(n - 1) + fibonacci(n - 2)

    memo[n] = f

    return f
