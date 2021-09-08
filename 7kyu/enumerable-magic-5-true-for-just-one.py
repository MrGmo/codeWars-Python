def one(sq,fun):
    count = 0
    for elem in sq:
        if fun(elem):
            count += 1
    if count == 1:
        return True
    return False