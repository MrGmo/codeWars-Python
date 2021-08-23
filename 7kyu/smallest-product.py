from functools import reduce

def smallest_product(a):
    smallest = float('inf')
    for elem in a:
        total = reduce(lambda x,y:x*y, elem)
        if total < smallest:
            smallest = total
    return smallest