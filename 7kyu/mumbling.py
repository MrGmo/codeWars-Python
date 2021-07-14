def accum(s):
    result_str = ''
    count = 1
    
    for char in s:
        result_str += char*count + '-'
        count += 1
    return result_str.title()[:-1]