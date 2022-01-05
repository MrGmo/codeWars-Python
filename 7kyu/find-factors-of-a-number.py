def factors(x):
    result = []
    if type(x) != int or x <= 0:
        return -1
    for num in range(x, 0, -1):
        if x % num == 0:
            result.append(num)
    return result
