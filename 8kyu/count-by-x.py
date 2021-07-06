def count_by(x, n):
    result = []
    for num in range(x, x*(n+1), x):
        result.append(num)
    return result