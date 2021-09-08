from functools import reduce 

def product(nums):
    try:
        return reduce(lambda x,y:x*y, nums)
    except:
        return None