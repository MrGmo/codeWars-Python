def buy(total, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == total and i != j:
                return [i, j]
    return None
