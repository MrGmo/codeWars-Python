import re

def filter_string(string):
    return int(re.sub('[\D]', '', string))