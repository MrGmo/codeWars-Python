def nth_fib(n):
    if n == 1:
        return 0
    if n < 4:
        return 1
    return nth_fib(n-1) + nth_fib(n-2)