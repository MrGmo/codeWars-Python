import re

def count_animals(s):
    nums_list = [int(x) for x in re.findall(r"\d+", s)]
    return sum(nums_list)
