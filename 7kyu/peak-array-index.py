def peak(arr):
    for i in range(len(arr)):
        if sum(arr[0:i+1]) == sum(arr[i:]):
            return i
    return -1