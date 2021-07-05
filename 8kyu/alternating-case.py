def to_alternating_case(string):
    arr = list(string)
    result = []
    
    for char in arr:
        if char == char.upper():
            result.append(char.lower())
        else:
            result.append(char.upper())
    return ''.join(result)