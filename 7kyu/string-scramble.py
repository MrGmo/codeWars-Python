def scramble(string, array):
    s = sorted(zip(string, array), key=lambda i: i[1])
    return "".join(i[0] for i in s)
