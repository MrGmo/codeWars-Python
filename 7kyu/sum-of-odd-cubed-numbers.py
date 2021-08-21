def cube_odd(arr):
    total = 0
    for num in arr:
        if type(num) != int:
            return None
        elif num % 2 != 0:
            total += (num**3)
        else:
            pass
    return total