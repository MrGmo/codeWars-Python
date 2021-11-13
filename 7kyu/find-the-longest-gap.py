import re

def gap(num):
    max_gap = 0
    temp_gap = 0
    bin_num = re.sub('0+$', '', bin(num)[2:])
    if '0' not in bin_num:
        return 0
    for char in bin_num:
        if char == '0':
            temp_gap += 1
            if temp_gap > max_gap:
                max_gap = temp_gap
        else:
            temp_gap = 0