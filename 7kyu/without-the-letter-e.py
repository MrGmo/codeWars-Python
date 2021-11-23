def find_e(s):
    if s == '':
        return ''
    if s == None:
        return None
    s = s.lower()
    if s.count('e') == 0:
        return 'There is no "e".'
    return str(s.count('e'))
