def generate_shape(n):
    result = ''
    for i in range(n):
        result += ('+'*n+'\n')
    return result[:-1]