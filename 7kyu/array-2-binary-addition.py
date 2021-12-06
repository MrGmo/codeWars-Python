def arr2bin(arr):
    if len([x for x in arr if type(x) != int]) > 0:
        return False
    return bin(sum(arr))[2:]
