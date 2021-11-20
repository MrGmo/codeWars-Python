def paul(x):
    total = 0
    obj = {
        'kata': 5,
        'Petes kata': 10,
        'life': 0,
        'eating': 1
        }
    for elem in x:
        if elem in obj:
            total += obj.get(elem)
    if total < 40:
        return 'Super happy!'
    elif 39 < total < 70:
        return 'Happy!'
    elif 69 < total < 100:
        return 'Sad!'
    else:
        return 'Miserable!'