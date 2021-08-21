def count(array):
    obj = {}
    for elem in array:
        if elem in obj:
            obj[elem] += 1
        else:
            obj[elem] = 1
    return obj