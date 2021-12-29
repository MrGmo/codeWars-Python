import re

def calculate(string):
    s = string.replace("loses", "-").replace("gains", "+")
    return eval(re.sub("[^0-9-+]", "", s))
