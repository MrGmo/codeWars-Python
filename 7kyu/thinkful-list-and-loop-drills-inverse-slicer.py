def inverse_slice(items, a, b):
    return [x for x in items if x not in items[a:b]]