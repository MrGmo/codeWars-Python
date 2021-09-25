def check_three_and_two(arr):
    obj = {}
    for elem in arr:
        if elem in obj:
            obj[elem] += 1
        else:
            obj[elem] = 1
    a = list(obj.values())
    if len(a) == 2 and 2 in a and 3 in a:
        return True
    return False