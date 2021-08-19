def fold_to(d):
    height = d
    times = 1
    fold = 2*0.0001
    if d < 0:
        return None
    if d < 0.0001:
        return 0
    while height > 0:
        height -= fold
        fold = fold*2
        times += 1
    return times