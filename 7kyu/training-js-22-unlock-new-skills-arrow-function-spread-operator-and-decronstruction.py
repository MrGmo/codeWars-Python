def shuffle_it(arr, *pairs):
    result = arr.copy()
    for i, j in pairs:
        result[i], result[j] = result[j], result[i]
    return result
