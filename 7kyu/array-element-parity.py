def solve(arr):
    for num in arr:
        try:
            if arr.index(-num) > -1:
                pass
        except:
            return num
