import functools

def sum_or_product(array, n):
    largest_sum = sum(sorted(array)[-n:])
    smallest_prod = functools.reduce(lambda x, y: x*y, sorted(array)[:n])
    if largest_sum > smallest_prod:
        return 'sum'
    elif largest_sum == smallest_prod:
        return 'same'
    return 'product'
