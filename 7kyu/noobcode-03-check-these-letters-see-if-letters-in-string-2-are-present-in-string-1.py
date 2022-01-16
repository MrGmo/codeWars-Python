def letter_check(arr):
    first, second = arr[0], arr[1]
    for i in range(len(arr[1])):
        if second[i].lower() in first.lower():
            pass
        else:
            return False
    return True
