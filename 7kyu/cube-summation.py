def cube_sum(n, m):
    min_num = min(n, m)+1
    max_num = max(n, m)+1
    return sum([x**3 for x in range(min_num, max_num)])
