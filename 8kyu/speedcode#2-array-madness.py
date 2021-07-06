def array_madness(a,b):
    squares = [x**2 for x in a]
    cubes = [x**3 for x in b]
    return sum(squares) > sum(cubes)