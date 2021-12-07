def is_very_even_number(n):
    nums = list(map(int, list(str(n))))
    if len(nums) == 1 and nums[0] % 2 == 0:
        return True
    if len(nums) == 1 and nums[0] % 2 != 0:
        return False
    return is_very_even_number(sum(nums))
