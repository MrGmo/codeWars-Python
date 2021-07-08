def char_freq(m):
    obj = {}
    for i in m:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    return obj