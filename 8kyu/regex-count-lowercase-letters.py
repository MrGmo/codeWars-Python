import re

def lowercase_count(string):
    return len(re.sub('[A-Z0-9\W_]', '', string))