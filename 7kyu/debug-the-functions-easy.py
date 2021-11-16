import functools

def multi(l):
    return functools.reduce(lambda x,y: x*y, l)
def add(l):
    return functools.reduce(lambda x,y: x+y, l)
def reverse(string):
    return string[::-1]