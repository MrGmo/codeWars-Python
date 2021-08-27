def solve(a,b):
    return ''.join([x for x in a if x not in b] + [y for y in b if y not in a])