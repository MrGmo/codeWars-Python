def move_zeros(array):
    count = array.count(0)
    new_arr = [x for x in array if x != 0]
    return new_arr + [0] * count
