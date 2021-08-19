def sum_triangular_numbers(n):
    total = []
    val = 0
    for i in range(0,n+1):
        total.append(i+val)
        val += i
    return sum(total)