def is_isogram(string):
    s = string.lower()
    return len(''.join(set(s))) == len(s)