def is_lucky(n):
    total = sum(map(int, list(str(n))))
    return total % 9 == 0 or total == 0
