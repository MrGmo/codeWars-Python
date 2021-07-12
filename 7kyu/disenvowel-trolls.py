import re

def disemvowel(st):
    return re.sub('[aeiouAEIOU]', '', st)