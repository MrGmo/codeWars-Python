def capitalize(s):
    caps = ''
    for i in range(len(s)):
        if i % 2 == 0:
            caps += s[i].upper()
        else:
            caps += s[i]
    return [caps,caps.swapcase()]