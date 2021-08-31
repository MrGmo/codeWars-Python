def switcher(arr):
    result = ''
    s = '*zyxwvutsrqponmlkjihgfedcba!? '
    for elem in arr:
        result += s[int(elem)]
    return result
    