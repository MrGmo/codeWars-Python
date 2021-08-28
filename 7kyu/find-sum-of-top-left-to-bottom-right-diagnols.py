def diagonal_sum(a):
    total = 0
    for i in range(len(a)):
        total += a[i][i]
    return total