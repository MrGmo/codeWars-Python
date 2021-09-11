def spacify(st):
    result = ''
    for char in st:
        if char.isalnum():
            result += char + ' '
        else:
            result += '  '
    return result[:-1]