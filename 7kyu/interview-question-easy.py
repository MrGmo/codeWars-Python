def get_strings(city):
    c = city.lower()
    obj = {}
    result = ''
    for char in c:
        if char in obj:
            obj[char] += '*'
        elif char == ' ':
            pass
        else:
            obj[char] = '*'
    for key,val in obj.items():
        result += key + ':' + val + ','
    return result[:-1]