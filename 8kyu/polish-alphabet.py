def correct_polish_letters(st):
    result = ''
    obj = {
        'ą':'a',
        'ć':'c',
        'ę':'e',
        'ł':'l',
        'ń':'n',
        'ó':'o',
        'ś':'s',
        'ź':'z',
        'ż':'z'
    }
    for char in st:
        if char in obj:
            result += obj.get(char)
        else:
            result += char
    return result