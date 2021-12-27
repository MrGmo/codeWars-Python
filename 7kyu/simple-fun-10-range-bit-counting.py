def range_bit_count(a, b):
    return "".join([bin(x)[2:] for x in list(range(a, b + 1))]).count("1")
