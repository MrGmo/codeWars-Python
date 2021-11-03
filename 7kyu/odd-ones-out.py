def odd_ones_out(nums):
    return [x for x in nums if nums.count(x) % 2 == 0]