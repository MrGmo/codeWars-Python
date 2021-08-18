import math

def circle_area(r):
    if type(r) == str:
        return False
    if r <= 0:
        return False
    return round(math.pi*r**2,2)