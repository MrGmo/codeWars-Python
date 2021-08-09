def max_multiple(div,bound):
    max_div = 0
    for i in range(1,bound+1):
        if i % div == 0 and i > max_div:
            max_div = i
    return max_div