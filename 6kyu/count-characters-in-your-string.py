def count(string):
    obj = {}
    for char in string:
        if char in obj:
            obj[char] += 1
        else:
            obj[char] = 1
    return obj