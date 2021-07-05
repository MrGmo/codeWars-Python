def index(array, n):
    if 0 <= n < len(array):
        return array[n]**n
    else:
        return -1