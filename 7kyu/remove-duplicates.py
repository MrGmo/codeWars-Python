def unique(ints):
    result = []
    for num in ints:
        if num in result:
            pass
        else:
            result.append(num)
    return result