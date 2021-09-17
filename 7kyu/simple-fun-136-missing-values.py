def missing_values(seq):
    x = [b for b in seq if seq.count(b) == 1][0]
    y = [a for a in seq if seq.count(a) == 2][0]
    return x*x*y