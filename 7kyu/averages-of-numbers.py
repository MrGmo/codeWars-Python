def averages(arr):
    result = []
    if arr == None or len(arr) == 0:
        return []
    for i in range(len(arr)-1):
        result.append((arr[i]+arr[i+1])/2)
    return result