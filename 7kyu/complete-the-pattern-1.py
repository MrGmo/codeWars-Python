def pattern(n):
    result = ''
    if n < 1:
        return ''
    for i in range(0,n+1):
        result += str(i)*i + '\n'
    return result[1:-1]