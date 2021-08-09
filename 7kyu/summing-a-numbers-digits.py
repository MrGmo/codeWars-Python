def sum_digits(num):
    return sum([int(x) for x in list(str(num).replace('-',''))])