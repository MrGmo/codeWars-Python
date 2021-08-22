def find_deleted_number(arr, mixed_arr):
    l = list(filter(lambda x:x not in mixed_arr, arr))
    return 0 if len(l) == 0 else l[0]