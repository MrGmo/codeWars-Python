def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())