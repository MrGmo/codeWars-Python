def cat_mouse(x):
    indx = 0
    for i in range(len(x)):
        if x[i] == 'C' or x[i] == 'm':
            indx += i
    return 'Escaped!' if indx > 4 else 'Caught!'