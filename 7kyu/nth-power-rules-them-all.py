def modified_sum(a,n):
    og_total = sum(a)
    exp = sum(list(map(lambda x: x**n, a)))
    return exp-og_total