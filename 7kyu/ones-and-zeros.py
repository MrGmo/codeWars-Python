def binary_array_to_number(arr):
    string = ''.join([str(x) for x in arr])
    return int(string, 2)