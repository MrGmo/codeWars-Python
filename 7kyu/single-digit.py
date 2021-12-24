def single_digit(n):
    num_sum = sum([int(x) for x in bin(n)[2:]])
    if len(str(n)) == 1:
        return n
    return single_digit(num_sum)
