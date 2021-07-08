def cube_checker(v, s):
    if v <= 0 or s <= 0:
        return False
    if s**3 == v:
        return True
    return False