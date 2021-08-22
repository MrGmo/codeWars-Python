def most_frequent_item_count(c):
    obj = {}
    if len(c) == 0:
        return 0
    for num in c:
        if num in obj:
            obj[num] += 1
        else:
            obj[num] = 1
    return max(obj.values())