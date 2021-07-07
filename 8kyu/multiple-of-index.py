def multiple_of_index(arr):
    result = []
    
    for num in range(1, len(arr)):
        if arr[num] % num == 0:
            result.append(arr[num])
    return result