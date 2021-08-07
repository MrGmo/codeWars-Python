import math

def factorial(n):
    if 0<=n<=12:
        return math.factorial(n)
    else:
        raise ValueError("value out of range")