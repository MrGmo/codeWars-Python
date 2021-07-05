def remove_every_other(my_list):
    result = []
    for elem in range(0, len(my_list), 2):
        result.append(my_list[elem])
    return result