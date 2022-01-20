def duplicate_sandwich(arr):
    between = []
    for i in range(len(arr)):
        if arr.count(arr[i]) == 2:
            between.append(i)
    return arr[between[0] + 1 : between[1]]
