import random

def generate(length):
    result = ''
    for i in range(length):
        result += str(random.randint(0,1))
    return result