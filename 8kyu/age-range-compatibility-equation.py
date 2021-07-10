import math

def dating_range(age):
    if age <= 14:
        miny = int(age-0.1*age)
        maxy = int(age+0.1*age)
        return f'{miny}-{maxy}'
    
    min = math.floor((age/2) + 7)
    max = math.floor((age-7)*2)
    return f'{min}-{max}'
    