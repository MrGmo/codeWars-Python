def men_from_boys(arr):
    odds = []
    evens = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return sorted(set(evens)) + sorted(set(odds))[::-1]