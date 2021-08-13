def gps(s, x):
    if len(x) < 2:
        return 0
    a = max(x[i] - x[i-1] for i in range(1, len(x))) 
    return a * 3600.0 / s