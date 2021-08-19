import math

def cooking_time(eggs):
    if eggs == 0:
        return 0
    return math.ceil((eggs/8))*5