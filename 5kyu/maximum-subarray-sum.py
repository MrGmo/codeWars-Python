def maxSequence(arr):
    current = 0
    max_found = 0
    for value in arr:
        current += value
        if current < 0:
            current = 0
        if current > max_found:
            max_found = current
    return max_found