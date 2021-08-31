def house_numbers_sum(inp):
    max_sum = 0
    temp = 0
    for num in inp:
        if num != 0:
            temp += num
            if temp > max_sum:
                max_sum = temp
        else:
            return max_sum
    return max_sum