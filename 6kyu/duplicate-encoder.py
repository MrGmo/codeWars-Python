def duplicate_encode(word):
    s = word.lower()
    obj = {}
    result = ''
    for char in s:
        if char in obj:
            obj[char] += 1
        else:
            obj[char] = 1
    for char in s:
        if obj[char] > 1:
            result += ')'
        else:
            result += '('
    return result