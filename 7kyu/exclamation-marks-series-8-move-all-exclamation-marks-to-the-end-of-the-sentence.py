def remove(s):
    total = s.count('!')
    return s.replace('!', '') + '!'*total
