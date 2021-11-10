def numbers(*args):
    for char in args:
        if type(char) == int or type(char) == float:
            pass
        else:
            return False
    return True