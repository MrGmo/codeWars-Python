import re

def zipvalidate(p):
    if p == '':
        return False
    if p[0] in ['0', '5', '7', '8', '9']:
        return False
    if ' ' in p:
        return False
    if p.isalpha():
        return False
    if len(p) != 6:
        return False
    if len(p) != len(re.sub('\D', '', p)):
        return False
    return True
