def add(*args):
    if len(args) == 0:
        return 0
    arr = list(args)
    total = 0
    for i in range(len(arr)):
        total += (i+1)*arr[i]
    return total