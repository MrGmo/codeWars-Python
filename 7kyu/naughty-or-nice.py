def get_nice_names(people):
    r = []
    for elem in people:
        if elem['was_nice'] == True:
            r.append(elem['name'])
    return r

def get_naughty_names(people):
    r = []
    for elem in people:
        if elem['was_nice'] == False:
            r.append(elem['name'])
    return r