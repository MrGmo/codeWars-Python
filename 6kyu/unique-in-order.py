def unique_in_order(iter):
    pre_item = None
    result = []
    
    for char in iter:
        if char != pre_item:
            result.append(char)
            pre_item = char
    return result