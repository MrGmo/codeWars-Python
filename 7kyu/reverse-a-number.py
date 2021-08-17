def reverse_number(n):
    r = False
    if n < 0:
        r = True
    n = list(str(n))[::-1]
    return -int(''.join(n)[:-1]) if r == True else int(''.join(n))