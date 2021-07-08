def multiply(n):
    new = abs(n)
    length = len(str(new))
    return -(5**length)*new if n < 0 else (5**length)*new