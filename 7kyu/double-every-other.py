def double_every_other(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 != 0:
            result.append(lst[i] * 2)
        else:
            result.append(lst[i])
    return result
