def powers_of_two(n):
    result = []
    
    for num in range(n+1):
        result.append(2**num)
    return result