def two_highest(arg1):
    a = list(set(arg1))
    b = sorted(a)
    return b[-2:][::-1]