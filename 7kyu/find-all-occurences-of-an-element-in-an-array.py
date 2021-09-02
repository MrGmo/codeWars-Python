def find_all(arr,n):
    result = []
    for i in range(len(arr)):
        if arr[i] == n:
            result.append(i)
    return result