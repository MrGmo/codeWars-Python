def reverse_it(data):
    if type(data) == int:
        return int(str(data)[::-1])
    if type(data) == float:
        return float(str(data)[::-1])
    if type(data) == str:
        return data[::-1]
    return data
