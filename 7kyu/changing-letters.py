def swap(s):
    result = ''
    for char in s:
        if char in 'aeiou':
            result += char.upper()
        else:
            result += char
    return result