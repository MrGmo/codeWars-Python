def sum_even_numbers(seq):
    total = 0
    for num in seq:
        if num % 2 == 0:
            total += num
    return total