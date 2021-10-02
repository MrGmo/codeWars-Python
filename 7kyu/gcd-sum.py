def solve(s,g):
    if s % g != 0:
        return -1
    else:
        return (g,s-g)