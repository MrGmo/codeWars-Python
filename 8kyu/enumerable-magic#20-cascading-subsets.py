def each_cons(lst, n):
    result = []
    count = 0
    while len(lst) >= n:
        result.append(lst[slice(count,n)])
        n += 1
        count += 1
    return result