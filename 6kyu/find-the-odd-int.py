def find_it(seq):
    obj = {}
    key_values = []
    for char in seq:
        if char in obj:
            obj[char] += 1
        else:
            obj[char] = 1
    for keys in obj.items():
        key_values.append(keys)
    return list(filter(lambda x: x[1]%2 != 0, key_values))[0][0]