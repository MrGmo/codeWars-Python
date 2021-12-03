def number_joy(n):
    n_sum = sum(map(int, list(str(n))))
    return n_sum * int(str(n_sum)[::-1]) == n
