def is_sorted_and_how(arr):
    asc = sorted(arr)
    des = sorted(arr)[::-1]
    
    if arr == asc:
        return 'yes, ascending'
    elif arr == des:
        return 'yes, descending'
    else:
        return 'no'