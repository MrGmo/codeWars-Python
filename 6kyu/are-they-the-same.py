def comp(a,b):
    try:
        return sorted([x**2 for x in a]) == sorted(b)
    except:
        return False
            