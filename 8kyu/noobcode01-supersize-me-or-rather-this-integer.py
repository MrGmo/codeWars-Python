def super_size(n):
    string = str(n)
    arr = [int(x) for x in string]
    sort = sorted(arr)[::-1]
    result = ''
    for char in sort:
        result += str(char)
    return int(result)