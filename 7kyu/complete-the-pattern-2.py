def pattern(n):
    result = ''
    times = n
    j = 0
    while times > 0:
        for i in range(n,j,-1):
            result += str(i)
        result += '\n'
        times -= 1
        j += 1
    return result[:-1]