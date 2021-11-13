import re

def remove(s):
    result = ''
    s = s.split(' ')
    for word in s:
        result += re.sub(r'!+$', '', word) + ' '
    return result[:-1]