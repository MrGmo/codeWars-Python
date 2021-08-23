def sum_of_digits(digits):
    if digits == None:
        return ''
    digits = str(digits)
    result = ''
    for num in digits:
        result += num + ' + '
    total = str(eval(result[:-3]))
    return result[:-2] + f'= {total}'