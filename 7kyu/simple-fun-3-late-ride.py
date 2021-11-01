def late_ride(n):
    h,m = divmod(n,60)
    return sum(map(int, list(f'{h}{m}')))