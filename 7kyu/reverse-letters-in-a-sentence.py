def reverser(s):
    s = s.replace(' ', '-').split('-')
    return '-'.join(list(map(lambda x: x[::-1], s))).replace('-', ' ')
    