def duplicate_elements(m, n):
    for num in m:
        if num in n:
            return True
    return False
