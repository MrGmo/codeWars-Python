def diff(a, b):
    a = set(a)
    b = set(b)
    return sorted(list(a.difference(b)) + list(b.difference(a)))
