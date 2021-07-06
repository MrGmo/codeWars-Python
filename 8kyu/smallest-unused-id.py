def next_id(arr):
    new_list = list(set(arr))
    compare_list = list(range(0,len(new_list)))
    
    for num in range(0, len(compare_list)):
        if compare_list[num] != new_list[num]:
            return compare_list[num]
    return 0 if len(compare_list) == 0 else compare_list[-1] + 1