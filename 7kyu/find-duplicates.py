def duplicates(arr):
    result = []
    temp = []
    for elem in arr:
        if elem not in temp:
            temp.append(elem)
        elif result.count(elem) < 1:
            result.append(elem)
        else:
            pass
    return result