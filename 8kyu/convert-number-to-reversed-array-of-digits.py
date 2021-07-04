def digitize(n):
    new_str = list(str(n)[::-1])
    return [int(num) for num in new_str]