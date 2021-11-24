def data_reverse(data):
    result_list = []
    for i in range(0, len(data), 8):
        result_list.append([data[i:i+8]])
    return sum(sum(result_list[::-1], []), [])
