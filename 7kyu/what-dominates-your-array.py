def dominator(arr):
    count = [x for x in arr if arr.count(x) > len(arr) / 2]
    if len(count) > 0:
        return count[0]
    return -1
