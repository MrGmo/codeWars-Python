def minMinMax(arr):
    small = min(arr)
    big = max(arr)
    minMin = 0
    for i in range(small, big+1):
        if i not in arr:
            minMin += i
            break
    return [small, minMin, big]
