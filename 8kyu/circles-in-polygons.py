from math import pi, sin, cos

def circle_diameter(sides, side_length):
    deg = pi / sides
    return side_length * cos(deg) / sin(deg)