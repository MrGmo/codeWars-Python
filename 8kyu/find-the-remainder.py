def remainder(a, b):
    large = max(a, b)
    small = min(a, b)
    try:
        return large % small
    except:
        return None
