def square_digits(n):
    result = ''
    for num in str(n):
        num = int(num)
        result += str(num**2)
    return int(result)