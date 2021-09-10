def explode(s):
    result = ''
    for char in s:
        result += char*int(char)
    return result