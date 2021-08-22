def max_diff(l):
    l = sorted(l)
    return l[-1]-l[0] if len(l) > 0 else 0