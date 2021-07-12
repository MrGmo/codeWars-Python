def high_and_low(numbers):
    num_list = [int(x) for x in numbers.split()]
    num_max = num_list[0]
    num_min = num_list[0]
    
    for num in num_list:
        if num > num_max:
            num_max = num
        if num < num_min:
            num_min = num
    return f'{num_max} {num_min}'