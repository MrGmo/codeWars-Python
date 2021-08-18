def switcheroo(s):
    result = ''
    for char in s:
        if char == 'a':
            result += 'b'
        elif char == 'b':
            result += 'a'
        else:
            result += char
    return result