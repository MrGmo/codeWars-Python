def find_digit(num,nth):
    if nth <= 0:
        return -1
    n = str(abs(num))[::-1]
    return int(n[nth-1]) if len(n) >= abs(nth) else 0