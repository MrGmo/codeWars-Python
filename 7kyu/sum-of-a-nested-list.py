def sum_nested(lst):
    arr = []
    for elem in lst:
        if type(elem) == list:
            arr = arr + elem
        else:
            arr.append(elem)
    for elem in arr:
        if type(elem) == int:
            pass
        else:
            return sum_nested(arr)
    return sum(arr)
