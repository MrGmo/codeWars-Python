from functools import reduce

def product_array(nums):
    result = []
    for i in range(len(nums)):
        r = reduce(lambda x,y: x*y, nums)
        result.append(r/nums[i])
    return result