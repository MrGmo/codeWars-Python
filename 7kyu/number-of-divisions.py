def divisions(n, div):
    count = 0
    while n > 1:
        n = n / div
        count += 1
    return count - 1
