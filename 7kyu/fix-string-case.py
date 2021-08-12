def solve(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        else:
            lower += 1
    return s.upper() if upper > lower else s.lower()