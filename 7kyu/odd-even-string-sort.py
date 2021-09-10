def sort_my_string(s):
    p1 = ''
    p2 = ''
    for i in range(len(s)):
        if i % 2 == 0:
            p1 += s[i]
        else:
            p2 += s[i]
    return p1 + ' ' + p2