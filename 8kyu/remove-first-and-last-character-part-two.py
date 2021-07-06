def array(string):
    new_str = string.split(',')[1:-1]
    
    if len(new_str) == 0:
        return None
    return ' '.join(new_str)