def solve(arr):
    result = []
    a = sorted(arr, reverse=True)
    while len(a) > 1:
        result.append(a.pop(0))
        result.append(a.pop())
        if len(a) == 1:
            result.append(a[0])
    return result