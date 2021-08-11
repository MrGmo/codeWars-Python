def show_sequence(n):
    if n < 0:
        return f'{n}<0'
    if n == 0:
        return '0=0'
    result = ''
    for i in range(n+1):
        result += str(i) + '+'
    return f'{result[:-1]} = {eval(result[:-1])}'