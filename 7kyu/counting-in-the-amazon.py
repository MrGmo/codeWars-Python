def count_arara(n):
    obj = {
        1:'anane',
        2:'adak'
    }
    result = ''
    start = 0
    while n != start:
        if n > 1:
            result += obj.get(2) + ' '
            n -= 2
        else:
            result += obj.get(1) + ' '
            n -= 1
    return result.strip()