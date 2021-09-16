def consecutive(arr):
    a = sorted(arr)
    if len(arr) <= 1:
        return 0
    new_arr = []
    for i in range(a[0],a[-1]+1):
        new_arr.append(i)
    return len(new_arr)-len(a)