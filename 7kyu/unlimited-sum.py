def sum(*args):
    total = 0
    for char in args:
        if type(char) == int:
            total += char
        else:
            pass
    return total