def create_array_of_tiers(n):
    n = str(n)
    result = []
    for i in range(len(n)):
        result.append(n[:i+1])
    return result