def solve(arr):
    result = []
    for index, item in enumerate(arr, 1):
        for val in arr[index:]:
            if item <= val:
                break
        else:
            result.append(item)
    return result