import re

def is_pangram(s):
    s = re.sub('[^a-z]', '',s.lower())
    return len(set(s)) == 26