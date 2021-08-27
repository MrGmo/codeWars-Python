def compare(s1,s2):
    if s1 == None:
        return True
    c1 = 0
    c2 = 0
    for char in s1:
        if char.isalpha():
            c1 += ord(char.upper())
        else:
            c1 = 0
    for char in s2:
        if char.isalpha():
            c2 += ord(char.upper())
        else:
            c2 = 0
    return c1 == c2