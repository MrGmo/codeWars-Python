from functools import reduce

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return reduce(lambda x, y: x + y, numbers)/len(numbers)