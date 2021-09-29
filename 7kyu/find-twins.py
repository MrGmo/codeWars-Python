def elimination(arr):
    obj = {}
    for char in arr:
        if char in obj:
            return char
        else:
            obj[char] = 1
    return None