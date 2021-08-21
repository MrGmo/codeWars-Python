def min_sum(arr):
    a = sorted(arr)
    total = 0
    while len(a) > 0:
        total += a.pop(0)*a.pop()
    return total