def narcissistic(v):
    s = list(str(v))
    length = len(s)
    numz = list(map(int, s))
    if length == 1:
        return True
    numz_list = [x**length for x in numz]
    return sum(numz_list) == v