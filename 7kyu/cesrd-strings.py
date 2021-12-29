def uncensor(inf, dis):
    result = ""
    replace = list(dis)
    for char in inf:
        if char == "*":
            result += replace.pop(0)
        else:
            result += char
    return result
