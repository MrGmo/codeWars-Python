def solve(s):
    up = 0
    low = 0
    num = 0
    special = 0
    for char in s:
        if char.isdigit():
            num += 1
        elif char.isupper():
            up += 1
        elif char.islower():
            low += 1
        else:
            special += 1
    return [up,low,num,special]