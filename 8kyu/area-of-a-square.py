import math

def square_area(a):
    radius = 4*a/(2*math.pi)
    return round((radius*2)**2/4, 2)