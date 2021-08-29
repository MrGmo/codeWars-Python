def hydrate(drink):
    d = drink.split()
    count = 0
    for char in d:
        if char.isdigit():
            count += int(char)
    return f'{count} glass of water' if count == 1 else f'{count} glasses of water'