import re

def borrow(s):
    s = s.lower()
    new = re.sub('[\W]', '', s)
    return new
