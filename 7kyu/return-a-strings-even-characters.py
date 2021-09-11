def even_chars(st):
    if len(st) < 2 or len(st) > 100:
        return 'invalid string'
    result = []
    for i in range(1, len(st)):
        if i % 2 != 0:
            result.append(st[i])
    return result