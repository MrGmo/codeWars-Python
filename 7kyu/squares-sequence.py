def squares(x,n):
    result = [x]
    if n <= 0:
        return []
    for i in range(1,n):
        result.append(x**2)
        x = result[-1]
    return result