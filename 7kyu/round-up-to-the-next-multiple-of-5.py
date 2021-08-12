def round_to_next5(n):
    next = 0
    if n == 0:
        return 0
    elif abs(n) % 5 == 0:
        return n
    elif n > 0:
        while next < n:
            next += 5
        return next
    else:
        while n < n+5:
            n += 1
            if n % 5 == 0:
                return n