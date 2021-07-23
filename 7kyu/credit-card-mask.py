import re

def maskify(cc):
    if len(cc) <= 4:
        return cc
    return re.sub('[a-z0-9]', '#', cc, len(cc)-4)