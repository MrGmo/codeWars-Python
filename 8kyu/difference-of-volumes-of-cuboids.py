from functools import reduce
import operator

def find_difference(a, b):
    return abs(reduce(operator.mul, a) - reduce(operator.mul, b))