import functools

def stray(arr):
    return functools.reduce(lambda x,y: x^y, arr)