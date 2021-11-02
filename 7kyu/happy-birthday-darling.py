import math

def womens_age(n):
    return f'{n}? That\'s just {20 if n % 2 == 0 else 21}, in base {math.floor(n/2)}!'
    