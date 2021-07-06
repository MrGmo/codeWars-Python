def correct(s):
    result_str = ''
    
    obj = {
        '5': 'S',
        '0': 'O',
        '1': 'I'
    }
    
    for char in s:
        if char in obj:
          result_str += obj.get(char)
        else:
          result_str += char
            
    return result_str