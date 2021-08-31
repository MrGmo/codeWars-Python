def max_gap(nums):
    n = sorted(nums)
    max_gap = 0
    for i in range(len(n)-1):
        gap = n[i+1]-n[i]
        if max_gap < gap:
            max_gap = gap
    return max_gap