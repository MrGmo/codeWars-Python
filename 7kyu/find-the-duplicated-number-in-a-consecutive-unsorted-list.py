def find_dup(arr):
    a = sorted(arr)
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return a[i]