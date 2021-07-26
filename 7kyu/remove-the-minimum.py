def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    m = min(numbers)
    c = numbers.copy()
    c.remove(m)
    return c