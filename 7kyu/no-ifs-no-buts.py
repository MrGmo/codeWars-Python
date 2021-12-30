def no_ifs_no_buts(a, b):
    while a < b:
        return f"{a} is smaller than {b}"
    while b < a:
        return f"{a} is greater than {b}"
    while b == a:
        return f"{a} is equal to {b}"
