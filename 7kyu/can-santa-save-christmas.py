def determine_time(arr):
    total = 0
    for time in arr:
        h, m, s = map(int, time.split(":"))
        total += h * 60 * 60 + m * 60 + s
    return total <= 24 * 60 * 60
