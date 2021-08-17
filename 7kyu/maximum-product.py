def adjacent_element_product(arr):
    max_mult = float('-inf')
    if len(arr) == 2:
        return arr[0]*arr[1]
    for i in range(len(arr)-1):
        if arr[i]*arr[i+1] > max_mult:
            max_mult = arr[i]*arr[i+1]
    return max_mult