def make_parts(arr, chunkSize):
    result = []
    for i in range(0, len(arr), chunkSize):
        result.append(arr[i : i + chunkSize])
    return result
