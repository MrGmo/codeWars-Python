def add_arrays(a1, a2):
    if len(a1) != len(a2):
        return RaiseValueError
    result = []
    for elem in range(0, len(a1)):
        if type(elem) == int:
            result.append(a1[elem] + a2[elem])
        else:
            result.append(str(a1[elem]) + str(a2[elem]))
    return result