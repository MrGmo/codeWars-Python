from itertools import accumulate

def barista(coffees):
    return sum(accumulate(sorted(coffees), lambda a, c: a + 2 + c))
