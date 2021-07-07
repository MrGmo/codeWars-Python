def check_exam(arr1,arr2):
    count = 0
    for i in range(0, len(arr1)):
        if arr1[i] == arr2[i]:
            count += 4
        if arr1[i] != arr2[i] and len(arr2[i]) != 0:
            count -= 1
    return count if count > 0 else 0