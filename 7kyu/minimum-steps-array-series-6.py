def minimum_steps(nums,val):
    n = sorted(nums)
    count = 0
    for indx,value in enumerate(n):
        count += value
        if count >= val:
            return indx