def decode(code, key):
    to_nums = [x + 96 for x in code]
    add_key = [int(x) for x in list(str(key))]
    result_str = ""
    temp_arr = []
    index = 0
    while len(to_nums) != len(add_key):
        add_key += [add_key[index]]
        index += 1
    for i in range(len(to_nums)):
        temp_arr.append(to_nums[i] - add_key[i])
    return "".join([chr(x) for x in temp_arr])
