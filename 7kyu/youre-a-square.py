import math

def is_square(n):
    if n < 0:
        return False
    return n == math.isqrt(n)**2