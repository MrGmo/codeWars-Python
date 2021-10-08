import math

def sillycase(silly):
    l = math.ceil(len(silly)/2)
    return silly[:l].lower() + silly[l:].upper()