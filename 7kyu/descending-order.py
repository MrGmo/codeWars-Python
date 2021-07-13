def descending_order(num):
    num_list = [int(x) for x in list(str(num))]
    sort_list = sorted(num_list, reverse = True)
    result_str = ""
    for char in sort_list:
        result_str += str(char)
    return int(result_str)