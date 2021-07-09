def merge_arrays(first, second):
    new_list = first + second
    new_set = set(new_list)
    return sorted(list(new_set))