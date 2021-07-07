def multi_table(number):
    result = ''
    for num in range(1, 11):
        mult = num * number
        result += f'{num} * {number} = {mult}' + '\n'
    return result[:-1]