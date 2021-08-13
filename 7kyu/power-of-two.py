import math

def power_of_two(x):
    if x == 0:
        return False
    log = round(math.log(x,2))
    return 2**log == x