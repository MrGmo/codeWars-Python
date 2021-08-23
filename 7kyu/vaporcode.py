def vaporcode(s):
    s = s.replace(' ', '')
    result = ''
    for char in s:
        result += char.upper() + '  '
    return result[:-2]