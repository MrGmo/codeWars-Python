def number_of_occurrences(element,sample):
    obj = {}
    for num in sample:
        if num in obj:
            obj[num] += 1
        else:
            obj[num] = 1
    return 0 if element not in sample else obj.get(element)