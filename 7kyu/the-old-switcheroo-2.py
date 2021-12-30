def encode(string):
    return "".join(f"{ord(x)-96}" if x.isalpha() else x for x in list(string.lower()))
