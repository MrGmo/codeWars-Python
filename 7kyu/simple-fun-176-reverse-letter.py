import re

def reverse_letter(string):
    return re.sub('[\d\W_]', '', string)[::-1]