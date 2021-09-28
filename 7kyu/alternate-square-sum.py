def alternate_sq_sum(arr):
    evens = []
    odds = []
    for i in range(len(arr)):
        if i % 2 != 0:
            evens.append(arr[i]**2)
        else:
            odds.append(arr[i])
    return sum(evens) + sum(odds)