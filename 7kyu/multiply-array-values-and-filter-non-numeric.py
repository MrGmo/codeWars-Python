def multiply_and_filter(seq, mult):
    return [x * mult for x in seq if type(x) == int or type(x) == float]
