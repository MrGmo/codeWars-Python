def find_sum(*args):
    if any(num < 0 for num in args):
        return -1
    return sum(args)