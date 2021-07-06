import re

def no_boring_zeros(n):
    if n == 0:
        return 0
    new_str = re.sub('0+$', '', str(n))
    return int(new_str)
    