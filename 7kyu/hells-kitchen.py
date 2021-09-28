import re

def gordon(a):
    a = a.upper().replace('A', '@')
    new_str = re.sub('[EIOU]', '*', a)
    result = [x + '!!!!' for x in new_str.split()]
    return ' '.join(result)