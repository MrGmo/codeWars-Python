def median(array):
    array.sort()
    if len(array) % 2 != 0:
        return array[len(array) // 2]
    mid_num = round(len(array) / 2)
    return (array[mid_num - 1] + array[mid_num]) / 2
