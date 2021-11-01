def spacey(array):
    result = []
    for i in range(len(array)):
        result.append(''.join(array[:i+1]))
    return result