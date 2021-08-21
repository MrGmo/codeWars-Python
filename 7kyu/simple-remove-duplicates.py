def solve(arr):
    result = []
    for i in range(len(arr)-1,-1,-1):
        if arr[i] in result:
            pass
        else:
            result.append(arr[i])
    return result[::-1]