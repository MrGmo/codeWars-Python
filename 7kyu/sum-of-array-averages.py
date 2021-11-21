import math

def sum_average(arr):
    total_sum = 0
    for elem in arr:
        total_sum += sum(elem)/len(elem)
    return math.floor(total_sum)