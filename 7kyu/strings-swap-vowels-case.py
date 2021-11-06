def swap_vowel_case(st):
    result = ''
    for char in st:
        if char in 'aeiouAEIOU':
            result += char.swapcase()
        else:
            result += char
    return result