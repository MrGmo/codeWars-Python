def consecutive(arr, a, b):
    x = arr.index(a)
    y = arr.index(b)
    return abs(x-y) == 1