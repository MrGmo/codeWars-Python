def hotpo(n):
    out = 0
    if n == 1:
        return 0
    else:
        while True:
            if n % 2 == 0:
                n = n / 2
                out += 1
            else:
                n = 3 * n + 1
                out += 1
            if  n == 1:
                break
    return out