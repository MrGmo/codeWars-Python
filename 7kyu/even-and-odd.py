def even_and_odd(n):
    even = ''
    odd = ''
    n = str(n)
    for char in n:
        if int(char) % 2 == 0:
            even += str(char)
        else:
            odd += str(char)
    if len(odd) == 0:
        odd = 0
    if len(even) == 0:
        even = 0
    return (int(even),int(odd))