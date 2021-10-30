import math

def is_square(arr):
    if len(arr) == 0:
        return None
    return [x for x in arr if x == math.isqrt(x)**2] == arr