def find_array(a1, a2):
    return [(i, x)[1] for i, x in enumerate(a1) if i in a2]
