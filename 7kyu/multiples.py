def multiple(x):
    if x % 15 == 0:
        return 'BangBoom'
    if x % 5 == 0:
        return 'Boom'
    if x % 3 == 0:
        return 'Bang'
    return 'Miss'