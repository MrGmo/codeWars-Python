def highest_value(a, b):
    a_sum = sum([ord(char) for char in list(a)])
    b_sum = sum([ord(char) for char in list(b)])
    if a_sum >= b_sum:
        return a
    return b
