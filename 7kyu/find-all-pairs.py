import math

def duplicates(arr):
    pairs = 0
    if len(arr) <= 1:
        return 0
    obj = {}
    for elem in arr:
        if elem in obj:
            obj[elem] += 1
        else:
            obj[elem] = 1
    vals = list(obj.items())
    for key, value in vals:
        if value > 1:
            pairs += math.floor(value/2)
    return pairs
    