def summy(string_of_ints):
    s = string_of_ints.split()
    return sum([int(x) for x in s])