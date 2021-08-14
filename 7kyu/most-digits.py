def find_longest(arr):
    most = ''
    for num in arr:
        if len(str(num)) > len(str(most)):
            most = num
    return most