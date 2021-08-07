def odd_or_even(arr):
    if len(arr) == 0:
        return [0]
    return 'odd' if sum(arr) % 2 != 0 else 'even'