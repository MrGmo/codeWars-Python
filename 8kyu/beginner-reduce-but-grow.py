from functools import reduce
import operator

def grow(arr):
    return reduce(operator.mul,arr)