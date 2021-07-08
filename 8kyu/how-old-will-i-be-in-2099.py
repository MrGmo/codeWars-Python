def calculate_age(yb, cy):
    if yb == cy:
        return 'You were born this very year!'
    if yb < cy:
        return f'You are {cy-yb} year old.' if (cy-yb) == 1 else f'You are {cy-yb} years old.'
    return f'You will be born in {yb-cy} year.' if (yb-cy) == 1 else f'You will be born in {yb-cy} years.'