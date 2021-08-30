def array_leaders(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] > sum(nums[i+1:]):
            result.append(nums[i])
    return result