def process_array(arr, callback):
    result = []
    for num in arr:
        result.append(callback(num))
    return result