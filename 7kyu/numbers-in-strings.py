def solve(s):
    max_num = '0'
    temp_num = '0'
    for char in s:
        if char.isdigit():
            temp_num += char
            if int(temp_num) > int(max_num):
                max_num = temp_num
        else:
            temp_num = ''
    return int(max_num)