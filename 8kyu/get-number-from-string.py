import re

def get_number_from_string(string):
    new_str = re.sub('\D', '', string)
    return int(new_str)