def populate_dict(keys, default):
    obj = {}
    for char in keys:
        if char in obj:
            obj[char] += 1
        else:
            obj[char] = default
    return obj