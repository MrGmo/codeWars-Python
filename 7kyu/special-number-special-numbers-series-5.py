def special_number(num):
    n = str(num)
    for char in n:
        if char not in '6789':
            pass
        else:
            return 'NOT!!'
    return 'Special!!'