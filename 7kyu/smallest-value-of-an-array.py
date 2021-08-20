def find_smallest(nums,to_return):
    min_num = min(nums)
    indx = nums.index(min_num)
    return min_num if to_return == 'value' else indx