def series_sum(n):
    if n == 0:
        return '0.00'
    if n == 1:
        return '1.00'
    sum = 1
    add = 4
    for i in range(2, n+1):
        sum += (1/add)
        add += 3
    return '{:.2f}'.format(sum)