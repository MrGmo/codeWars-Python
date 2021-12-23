def battle(x, y):
    a = sum([ord(i) - 64 for i in x])
    b = sum([ord(i) - 64 for i in y])
    if a > b:
        return x
    elif b > a:
        return y
    else:
        return "Tie!"
