def is_divisible(*args):
    nums = list(args)
    first = nums[0]
    for i in range(1,len(nums)):
        if first % nums[i] == 0:
            pass
        else:
            return False
    return True