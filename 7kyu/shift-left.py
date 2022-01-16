def shift_left(a, b):
    a = list(a)
    b = list(b)
    count = 0
    while a != b:
        if len(a) > len(b):
            a.pop(0)
            count += 1
            if a == b:
                return count
        else:
            b.pop(0)
            count += 1
            if a == b:
                return count
    return count
