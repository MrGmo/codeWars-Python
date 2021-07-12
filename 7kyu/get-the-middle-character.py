import math

def get_middle(s):
    start = math.floor(len(s)/2)
    if len(s) % 2 == 0:
        return s[start-1:start+1]
    return s[start]