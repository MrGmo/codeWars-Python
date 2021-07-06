def well(x):
    if x.count('good') == 0:
        return 'Fail!'
    if x.count('good') < 3:
        return 'Publish!'
    return 'I smell a series!'