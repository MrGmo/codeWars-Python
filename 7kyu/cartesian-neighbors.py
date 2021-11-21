def cartesian_neighbor(x,y):
    return [(a,b) for a in range(x-1,x+2) for b in range(y-1,y+2) if (a,b) != (x,y)]