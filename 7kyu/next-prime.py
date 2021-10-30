import math

def next_prime(n):
    if n == 0:
        return 2
    if is_prime(n+1):
        return n+1
    return next_prime(n+1)

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True