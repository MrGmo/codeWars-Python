def find(n):
    return sum([x for x in range(0,n+1) if x % 3 == 0 or x % 5 == 0])