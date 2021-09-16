def triple_x(s):
    for x in range(len(s)):
        if s[x] == 'x':
            return s[x+1:x+3] == 'xx'
    return 0