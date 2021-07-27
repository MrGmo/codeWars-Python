import math

def find_next_square(sq):
    num = sq + 1
    if sq != math.isqrt(sq)**2:
        return -1
    while num != math.isqrt(num)**2:
        num += 1
    return num