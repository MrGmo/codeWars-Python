def two_sort(array):
    result = ''
    first_val = sorted(array)[0]
    
    for char in first_val:
        result += char + '***'
    
    return result[:-3]