def elevator_distance(arr):
    total = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            total += (arr[i]-arr[i+1])
        else:
            total += (arr[i+1]-arr[i])
    return total