def partlist(arr):
    new_arr = []
    for x in range(1,len(arr)):
        y = ' '.join(arr[:x])
        z = ' '.join(arr[x:])
        new_arr.append((y,z))
    return new_arr