def is_monotone(h):
    for i in range(len(h)-1):
        if h[i] <= h[i+1]:
            pass
        else:
            return False
    return True