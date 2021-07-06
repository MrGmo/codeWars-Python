def stringy(size):
    result = ''
    for i in range(1, size+1):
        if i % 2 != 0:
            result += '1'
        else:
            result += '0'
    return result