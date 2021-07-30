import functools

def persistence(n, count = 0):
    s = [int(x) for x in list(str(n))]
    if len(s) == 1:
        return count
    reduce_num = functools.reduce(lambda x, y: x*y, s)
    return persistence(reduce_num, count+1)