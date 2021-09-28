def sum_square_even_root_odd(nums):
    new_arr = []
    for num in nums:
        if num % 2 == 0:
            new_arr.append(num**2)
        else:
            new_arr.append(num**(1/2))
    return round(sum(new_arr),2)