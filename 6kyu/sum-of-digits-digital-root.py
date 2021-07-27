import functools

def digital_root(n):
    s = list(str(n))
    num_list = list(map(int, s))
    if len(num_list) == 1:
        return num_list[0]
    helper = functools.reduce(lambda x, y: x +y, num_list)
    return digital_root(helper)