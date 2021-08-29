def even_last(nums):
    if len(nums) == 0:
        return 0
    last = nums[-1]
    total = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            total += nums[i]
        else:
            pass
    return total*last