def ordered_count(inp):
    result = []
    obj = {}
    for char in inp:
        if char in obj:
            obj[char] += 1
        else:
            obj[char] = 1
    for value,num in obj.items():
        result.append((value,num))
    return result