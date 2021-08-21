def div_con(x):
    total = 0
    for elem in x:
        if type(elem) == str:
            total -= int(elem)
        else:
            total += elem
    return total