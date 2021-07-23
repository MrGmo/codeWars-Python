import re

def xo(s):
    new_str = re.sub('[^oxOX]', '', s)
    x_str = re.sub('[^xX]', '', new_str)
    if len(new_str)/2 == len(x_str):
        return True
    return False