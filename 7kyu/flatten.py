def flatten(lst):
    result = []
    for arr in lst:
        if type(arr) == list:
            for x in arr:
                result.append(x)
        else:
            result.append(arr)
    return result