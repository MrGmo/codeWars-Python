def next_happy_year(year):
    y = year+1
    is_true = len(list(str(y))) == len(set(str(y)))
    while is_true == False:
        y += 1
        is_true = len(list(str(y))) == len(set(str(y)))
    return y