def first_non_consecutive(arr):
    if len(arr) < 2:
        return None

    for i in range(len(arr)-1):
      diff = arr[i+1] - arr[i]
      if diff != 1:
        return arr[i+1]
    return None