def is_vow(inp):
    vow_nums = [97, 101, 105, 111, 117]
    result = []
    
    for num in inp:
        if num in vow_nums:
            result.append(chr(num))
        else:
            result.append(num)
    return result