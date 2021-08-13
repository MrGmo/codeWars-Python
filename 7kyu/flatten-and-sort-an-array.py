def flatten_and_sort(array):
    result = []
    for arr in array:
        if type(arr) == list:
            for x in arr:
                result.append(x)
        else:
            result.append(arr)
    return sorted(result)