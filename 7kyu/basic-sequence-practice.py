def sum_of_n(n):
    result = []
    x = 0
    if n > 0:
        for i in range(x,n+1):
            result.append(i+x)
            x += i
        return result
    else:
        for j in range(x,n-1,-1):
            result.append(j-x)
            x -= j
        return result