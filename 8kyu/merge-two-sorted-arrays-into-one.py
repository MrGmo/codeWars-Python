def merge_arrays(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return []
    
    both = set(arr1 + arr2)
    
    return sorted(list(both))