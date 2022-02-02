def remainder(dividend, divisor):
    while divisor <= dividend:
        dividend -= divisor
    return dividend
