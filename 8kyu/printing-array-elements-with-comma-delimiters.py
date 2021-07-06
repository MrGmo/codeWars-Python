def print_array(arr):
    result = ''
    for char in arr:
        result += ',' + str(char)
    return result[1:]