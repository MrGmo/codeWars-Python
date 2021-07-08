def derive(coefficient, exponent):
    part1 = str(coefficient * exponent)
    minus1 = str(exponent-1)
    return part1 + 'x^' + minus1
    