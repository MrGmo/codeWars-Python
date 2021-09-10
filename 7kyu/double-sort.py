def db_sort(arr):
    nums = []
    lets = []
    for char in arr:
        if type(char) == int:
            lets.append(char)
        else:
            nums.append(char)
    return sorted(lets) + sorted(nums)