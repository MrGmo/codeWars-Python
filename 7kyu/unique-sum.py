def unique_sum(l):
    if len(l) == 0:
        return None
    return sum(list(set(l)))