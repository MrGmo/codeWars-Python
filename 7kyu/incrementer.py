def incrementer(nums):
    return [ (v+i)%10 for i,v in enumerate(nums,1) ]