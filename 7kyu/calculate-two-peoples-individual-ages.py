def get_ages(s, diff):
    old = ((s-diff)/2) + diff
    young = (s-diff)/2
    if old < 0 or young < 0:
        return None
    if young > old:
        return None
    return (old, young)
