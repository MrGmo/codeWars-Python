def find_secret_number(low, high, f):
    while low <= high:
        mid = (low + high) // 2
        r = f.guess_number(mid)
        if r == "Larger":
            low = mid + 1
        elif r == "Smaller":
            high = mid - 1
        else:
            return mid
