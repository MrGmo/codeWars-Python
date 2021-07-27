def array_diff(a, b):
    result = []
    for num in a:
        if num not in b:
            result.append(num)
    return result