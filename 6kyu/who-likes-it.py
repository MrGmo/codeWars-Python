def likes(names):
    s = ' like this'
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return names[0] + ' likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]}' + s
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]}' + s
    return f'{names[0]}, {names[1]} and ' + str(len(names)-2) + ' others' + s