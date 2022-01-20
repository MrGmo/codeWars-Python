def find_missing(arr1, arr2):
    a1 = sorted(arr1)
    a2 = sorted(arr2)
    for i in range(len(a2)):
        if a1[i] != a2[i]:
            return a1[i]
    return a1[-1]
