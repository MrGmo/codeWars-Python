def printer_error(s):
    count = 0
    s = list(s)
    for char in s:
        if ord(char) > 109:
            count += 1
    return f'{count}' + f'/{len(s)}'